---
title: Yolov5 Sunspot Hunter
emoji: 🌟
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 4.12.0
app_file: app.py
pinned: false
license: ecl-2.0
---

# YOLOv5 Sunspot Hunter 🌟

Explore the dynamic solar surface with the YOLOv5 Sunspot Hunter! This application is designed to detect and analyze sunspots using state-of-the-art object detection technology.

## Developer

Developed by Ramon Mayor Martins (2023)

- Email: [rmayormartins@gmail.com](mailto:rmayormartins@gmail.com)
- Homepage: [https://rmayormartins.github.io/](https://rmayormartins.github.io/)
- Twitter: [@rmayormartins](https://twitter.com/rmayormartins)
- GitHub: [https://github.com/rmayormartins](https://github.com/rmayormartins)
- my Radio Callsign (PU4MAY) Brazil

## About the Project

This tool using YOLOv5, an advanced neural network, for the detection and classification (hunting) of sunspots. The sunspot images were collected from several high-quality sources, including the SOHO satellite, and other NASA and ESA archives, under Creative Commons licenses. These images were then annotated with precision using Makesense.ai.

## Key Features

- **Image Source:** The sunspot images were sourced from SOHO satellite, NASA, and ESA archives.
- **Labeling:** Annotations were done using Makesense.ai.
- **Model Training:** The model was trained with YOLOv5, achieving satisfactory metrics including mAP (mean Average Precision).
- **Model File:** The 'best.pt' file is used, which represents the model's optimal state after training.

## How to Use

- **Launch:** Start the YOLOv5 Sunspot Hunter by running the `app.py` script in Gradio.
- **Image Upload:** Users can upload their own images of the sun or utilize current solar images from websites like [Space Weather Live](https://www.spaceweatherlive.com/en/solar-activity.html), [LMSAL](https://www.lmsal.com/solarsoft/latest_events/), [SOHO Realtime Images](https://soho.nascom.nasa.gov/data/realtime-images.html), and [The Sun Today](https://www.thesuntoday.org/sun/current-observations/).
- **Detection:** The tool processes the uploaded image, identifying and highlighting sunspots with high precision.
- **Results:** View the results instantly, with sunspots clearly marked and classified.

## Feedback and Contributions

Feel free to reach out or contribute to the project. Your feedback and contributions are highly appreciated!

## License

This project is released under the ECL-2.0 license.

## Acknowledgments

Special thanks to the teams at NASA, ESA, and SOHO for providing valuable solar data.

---
*Check out the configuration reference at [Hugging Face Spaces Config Reference](https://huggingface.co/docs/hub/spaces-config-reference).*


