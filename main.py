# import streamlit as st
# import numpy as np
# from PIL import Image
# from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
# from tensorflow.keras.preprocessing.image import img_to_array

# # モデルの読み込み（ImageNetで学習済みのResNet50）
# model = ResNet50(weights='imagenet')

# st.title("犬・猫判定アプリ 🐶🐱")

# # 画像アップローダー
# uploaded_file = st.file_uploader("画像をアップロードしてください（犬 or 猫）", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file).convert('RGB')
#     st.image(image, caption='アップロードされた画像', use_column_width=True)

#     # 推論処理
#     if st.button("判定する"):
#         st.write("判定中です...")
#         # 画像前処理
#         img_resized = image.resize((224, 224))
#         x = img_to_array(img_resized)
#         x = np.expand_dims(x, axis=0)
#         x = preprocess_input(x)

#         preds = model.predict(x)
#         decoded = decode_predictions(preds, top=3)[0]

#         # 結果表示（犬・猫に限定して表示）
#         found = False
#         for _, label, prob in decoded:
#             if "dog" in label or "cat" in label:
#                 st.success(f"これは **{label.replace('_', ' ')}** です！ (確信度: {prob:.2%})")
#                 found = True
#                 break

#         if not found:
#             st.warning("犬か猫の画像ではない可能性があります。")
import streamlit as st
from utils import load_model, predict_image
from logger import get_logger
from PIL import Image

# ロガーの準備
logger = get_logger()

# タイトル
st.title("犬 or 猫 判定アプリ")

# モデルロード
model = load_model("model/model.h5")

# 画像アップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロード画像", use_container_width=True)

    with st.spinner("判定中..."):
        prediction = predict_image(model, image)
        st.success(f"この画像は「{prediction}」です。")
        logger.info(f"予測: {prediction}")
