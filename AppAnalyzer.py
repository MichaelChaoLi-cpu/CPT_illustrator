
from joblib import dump, load
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow.keras as keras
import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model
from transformers import TFBertModel


class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1, 
                 name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.ff_dim = ff_dim
        self.rate = rate
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)
        

    def get_config(self):
        config = super().get_config()
        config.update({
            'embed_dim': self.embed_dim,
            'num_heads': self.num_heads,
            'ff_dim': self.ff_dim,
            'rate': self.rate
        })
        return config    

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)


def precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def recall(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    actual_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (actual_positives + K.epsilon())
    return recall

def ModelLoader(Model_Address):
    custom_objects = {
        'TFBertModel': TFBertModel,
        'TransformerBlock': TransformerBlock
    }
    try:
        model = load_model(Model_Address, custom_objects=custom_objects)
    except:
        with keras.utils.custom_object_scope({'precision': precision, 'recall': recall}):
            model = keras.models.load_model(Model_Address, custom_objects=custom_objects)
    return model


DataX = load('TempPDF/total_txt.joblib')

model = ModelLoader('CPT_demo_2_378k_i0.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i0.joblib')
mean_i0 = np.mean(y_pred)
print("Community done")

model = ModelLoader('CPT_demo_2_378k_i1.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i1.joblib')
mean_i1 = np.mean(y_pred)
print("Air Pollution done")

model = ModelLoader('CPT_demo_2_378k_i2.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i2.joblib')
mean_i2 = np.mean(y_pred)
print("Greenhouse Gas done")

model = ModelLoader('CPT_demo_2_378k_i3.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i3.joblib')
mean_i3 = np.mean(y_pred)
print('Water Consumption done')

model = ModelLoader('CPT_demo_2_378k_i4.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i4.joblib')
mean_i4 = np.mean(y_pred)
print('Mining Consumption done')

model = ModelLoader('CPT_demo_2_378k_i5.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i5.joblib')
mean_i5 = np.mean(y_pred)
print("Work Environment done")

model = ModelLoader('CPT_demo_2_378k_i6.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i6.joblib')
mean_i6 = np.mean(y_pred)
print("Safety_Health done")

model = ModelLoader('CPT_demo_2_378k_i7.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i7.joblib')
mean_i7 = np.mean(y_pred)
print('Human_Right done')

model = ModelLoader('CPT_demo_2_378k_i8.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i8.joblib')
mean_i8 = np.mean(y_pred)
print('Governance_Risk done')

model = ModelLoader('CPT_demo_2_378k_i9.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i9.joblib')
mean_i9 = np.mean(y_pred)
print('Production_Cost done')

model = ModelLoader('CPT_demo_2_378k_i10.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i10.joblib')
mean_i10 = np.mean(y_pred)
print('Domestic_Job done')

model = ModelLoader('CPT_demo_2_378k_i11.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i11.joblib')
mean_i11 = np.mean(y_pred)
print('Economic Ripple done')

model = ModelLoader('CPT_demo_2_378k_i12.h5')
y_pred = model.predict(DataX)
y_pred = y_pred[:,1]
dump(y_pred, 'TempPDF/i12.joblib')
mean_i12 = np.mean(y_pred)
print('Domestic Reflux done')

mean_list = [mean_i0, mean_i1, mean_i2, mean_i3, mean_i4, mean_i5,
             mean_i6, mean_i7, mean_i8, mean_i9, mean_i10, mean_i11,
             mean_i12]
dump(mean_list, 'TempPDF/AllIndex.joblib')

"""
from joblib import dump, load
import numpy as np
y_pred = load('TempPDF/i0.joblib')
mean_i0 = np.mean(y_pred)

y_pred = load('TempPDF/i1.joblib')
mean_i1 = np.mean(y_pred)

y_pred = load('TempPDF/i2.joblib')
mean_i2 = np.mean(y_pred)

y_pred = load('TempPDF/i3.joblib')
mean_i3 = np.mean(y_pred)

y_pred = load('TempPDF/i4.joblib')
mean_i4 = np.mean(y_pred)

y_pred = load('TempPDF/i5.joblib')
mean_i5 = np.mean(y_pred)

y_pred = load('TempPDF/i6.joblib')
mean_i6 = np.mean(y_pred)

y_pred = load('TempPDF/i7.joblib')
mean_i7 = np.mean(y_pred)

y_pred = load('TempPDF/i8.joblib')
mean_i8 = np.mean(y_pred)

y_pred = load('TempPDF/i9.joblib')
mean_i9 = np.mean(y_pred)

y_pred = load('TempPDF/i10.joblib')
mean_i10 = np.mean(y_pred)

y_pred = load('TempPDF/i11.joblib')
mean_i11 = np.mean(y_pred)

y_pred = load('TempPDF/i12.joblib')
mean_i12 = np.mean(y_pred)

mean_list = [mean_i0, mean_i1, mean_i2, mean_i3, mean_i4, mean_i5,
             mean_i6, mean_i7, mean_i8, mean_i9, mean_i10, mean_i11,
             mean_i12]
dump(mean_list, 'TempPDF/AllIndex.joblib')
"""


