import numpy as np
from PIL import Image
import streamlit as st
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

def load_model(path=None):
    # pathは使わないが、引数として残してもOK
    model = ResNet50(weights='imagenet')
    return model

def predict_image(model, image):
    # ResNet50用に 224x224 にリサイズ
    image = image.resize((224, 224))

    img_array = np.array(image)

    # 透明度チャンネル（α）がある場合は削除（RGBにする）
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    # バッチ次元を追加
    img_array = np.expand_dims(img_array, axis=0)

    # ImageNetの前処理（正規化など）
    img_array = preprocess_input(img_array)

    # 予測
    preds = model.predict(img_array)

    # 上位1件をデコード
    decoded = decode_predictions(preds, top=1)[0][0]
    class_name = decoded[1]
    confidence = decoded[2]

    if "cat" in class_name.lower():
        return f"猫（{class_name}, 確信度: {confidence:.2f}）"
    elif "dog" in class_name.lower():
        return f"犬（{class_name}, 確信度: {confidence:.2f}）"
    else:
        return f"不明（{class_name}, 確信度: {confidence:.2f}）"