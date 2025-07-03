import streamlit as st
import pickle
from PIL import Image


def main():
    st.set_page_config(page_title="Weather Prediction App", layout="centered")

    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "home"


    # Navigation logic
    def go_to_prediction():
        st.session_state.page = "predict"


    def go_home():
        st.session_state.page = "home"


    def go_about():
        st.session_state.page = "about"





    # App Layout
    if st.session_state.page == "home":
        st.markdown(
            """
            <style>
            .stApp {
                background-image: url('https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=600');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            # .block-container {
            #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
            #     padding: 2rem;
            #     border-radius: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style='background-color:; padding: 20px; border-radius: 10px;'>
                <h1 style='color: white; text-align: center; font-family: "Georgia", monospace;'>
                    🌤️ WEATHER PREDICTION MODEL
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
                    <style>
                    @keyframes fadeIn {
                        0% { opacity: 0; }
                        100% { opacity: 1; }
                    }

                    .fade-text {
                        animation: fadeIn 3s ease-in-out;
                        font-size: 26px;
                        color: #255,255;
                        text-align: center;
                        margin-top: 30px;
                    }
                    </style>

                    <div class="fade-text">
                        🌤 Welcome to the Weather Prediction 
                    </div>
                """, unsafe_allow_html=True)
        st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        st.markdown("Here You Can Predict Sample Weathers.")
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.button("Go to Prediction", on_click=go_to_prediction)
        st.button("About", on_click=go_about)


    elif st.session_state.page == "predict":
        st.title("📈 Weather Prediction")
        temp_max = st.number_input("Temp_max (°C)")
        temp_min = st.number_input("Temp_min (°C)")
        precipitation = st.number_input("Humidity (%)")
        wind = st.number_input("Wind (mph)")
        features=[temp_max,temp_min,precipitation,wind]
        #scaler = pickle.load(open('minmax (1).sav', 'rb'))
        #models = pickle.load(open('model.sav', 'rb'))
        with open ('scaler_new.sav','rb')as f:
            scaler = pickle.load(f)
        with open('model.sav','rb')as f:
            models = pickle.load(f)
        st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
        if st.button("Predict Weather"):
            scaled = scaler.transform([features])
            print("scaler applied Successfully",scaled)
            result = models.predict(scaler.transform([features]))
            if result==0:
                    st.write("# It's Drizzle today")

            # Custom HTML for background GIF
                    st.markdown(
                    """
                    <style>
                    .stApp {
                        background-image: url('https://i.gifer.com/srG.gif');
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                        background-attachment: fixed;
                    }
                    # .block-container {
                    #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
                    #     padding: 2rem;
                    #     border-radius: 10px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True)

            elif result==1:
                    st.write("# It's Fog today")
                    # Custom HTML for background GIF
                    st.markdown(
                        """
                        <style>
                        .stApp {
                            background-image: url('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZodjJyNG1hdG5zNG83dzJmYWFzMzA5NjF5MnUzeXp3bTZwMmphZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ZWRCWdUymIGNW/giphy.gif');
                            background-size: cover;
                            background-position: center;
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                        }
                        # .block-container {
                        #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
                        #     padding: 2rem;
                        #     border-radius: 10px;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True)
            elif result==2:
                    st.write("# It's Rainy today")
                    # Custom HTML for background GIF
                    st.markdown(
                        """
                        <style>
                        .stApp {
                            background-image: url('https://cdn.pixabay.com/animation/2023/02/15/02/20/02-20-04-915_512.gif');
                            background-size: cover;
                            background-position: center;
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                        }
                        # .block-container {
                        #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
                        #     padding: 2rem;
                        #     border-radius: 10px;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True)

            elif result==3:
                    st.write("# It's Snow today")
                    # Custom HTML for background GIF
                    st.markdown(
                        """
                        <style>
                        .stApp {
                            background-image: url('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm5vaTZqeXRycXR1OGQwdjRkeDE4enVpMmN6YXczeHYyMGc2cDd1eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BDucPOizdZ5AI/giphy.gif');
                            background-size: cover;
                            background-position: center;
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                        }
                        # .block-container {
                        #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
                        #     padding: 2rem;
                        #     border-radius: 10px;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True)


            else:
                    st.write("# It's Sunny today")
                # Custom HTML for background GIF
                    st.markdown(
                    """
                    <style>
                    .stApp {
                        background-image: url('https://i.gifer.com/CZx.gif');
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                        background-attachment: fixed;
                    }
                    # .block-container {
                    #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
                    #     padding: 2rem;
                    #     border-radius: 10px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                    )

        st.button("⬅️ Back to Home", on_click=go_home)

    elif st.session_state.page == "about":
        st.title("ℹ️ About This Model")
        st.markdown("""
            This is a simple weather prediction model interfaced by Streamlit.
            

            It takes inputs such as :
            - Temperature
            - Humidity
            - Pressure
            - Wind
            - Precipitation

            ...and predicts if it's **Sunny**, **Rainy**, **Cloudy**, **Snow**, **Fog**.
            """)


        st.markdown("### 🔗 Resources")
        st.markdown("## 📓 Google Colab Notebook")
        st.markdown("- [📓 Google Colab](https://colab.research.google.com/drive/1uTJBKnZGOzQ_QQzezeYAM2eGvjH_0FlQ#scrollTo=6s313Lo-ZfHi)")
        st.markdown("## 📁 Dataset")
        st.markdown("- [📊 Dataset CSV](https://www.kaggle.com/datasets/ananthr1/weather-prediction)")


        st.markdown(
            """
            <style>
            .stApp {
                background-image: url('https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=600');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            # .block-container {
            #     background-color: rgba(255, 255, 255, 0.85); /* White background with some transparency */
            #     padding: 2rem;
            #     border-radius: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        st.button("⬅️ Back to Home", on_click=go_home)


    Pages = [
        st.Page(go_home, title='Home'),
        st.Page(go_to_prediction, title="Prediction"),
        st.Page(go_about, title="About")
    ]

    with st.sidebar:
        st.title("Weather Prediction")
        selected = st.navigation(Pages, position="sidebar")
    selected.run()


main()

