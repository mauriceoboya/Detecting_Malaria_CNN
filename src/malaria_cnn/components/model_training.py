import time
import os
import urllib.request as request
import zipfile
import tensorflow as tf
import time
from pathlib import Path
from malaria_cnn.entity.config_entity import PrepareCallbacksConfig,TrainingConfig


class PrepareCallbacks:
    def __init__(self,config:PrepareCallbacksConfig):
        self.config=config
    
    @property
    def _create_tb_callbacks(self):
        timestamp=time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_dir=os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",      
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_dir)
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_weights_only=True,
            save_best_only=True
        )
    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None  # Initialize model attribute

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_model_path)

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.2
        )
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.Training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )
            self.train_generator = train_datagenerator.flow_from_directory(
                directory=self.config.Training_data,
                subset='training',
                shuffle=True,
                **dataflow_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.Training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self, callback_list: list):
        if self.model is None:
            self.get_base_model()  # Ensure model is loaded before training

        self.train_valid_generator()  # Ensure generators are initialized

        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        # Recreate optimizer to ensure compatibility with the new model
        optimizer = tf.keras.optimizers.Adam()  # Modify with your optimizer and settings

        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

        self.model.fit(
            self.train_generator,
            steps_per_epoch=self.steps_per_epoch,
            epochs=self.config.params_epochs,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps,
            callbacks=callback_list
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)