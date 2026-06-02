<div align="center">

<img src="https://www.sju.edu.in/assets/img/st-joseph-university-logo.png" height="80" style="background:white; padding:8px; margin:0 16px;" />
<img src="https://www.erafoundationindia.org/images/logo.svg" height="80" style="background:white; padding:8px; margin:0 16px;" />
<img src="https://comedkares.org/wp-content/uploads/2023/04/Comedkares-Logo-EPS.png" height="80" style="background:white; padding:8px; margin:0 16px;" />

</div>

---

# AI-Based Food Package Inspection System Using YOLO and Raspberry Pi

<div align="center">

**Manish J C**, MSc BDA, 252BDA59 &nbsp;·&nbsp; **Lydia Thangam S**, MSc BDA, 252BDA24 &nbsp;·&nbsp;**Steffi Merlin P**, MCA, 253MCA13 &nbsp;·&nbsp; **Adone Kurian**, MCA, 253MCA19 &nbsp;·&nbsp; **P R Vishnu Prasad**, MCA, 253MCA26

</div>

---

## Abstract

Ensuring proper food packaging is a critical requirement in the food industry to maintain product quality, safety, and customer satisfaction. This project presents an AI-based food package inspection system that automatically detects whether a food product is packaged correctly or not using computer vision and deep learning techniques. The system employs a camera connected to a Raspberry Pi to capture real-time images of food packages, which are then analyzed using the YOLO (You Only Look Once) object detection algorithm implemented in Python. The YOLO model is trained on a custom dataset containing images of both correctly packaged and defective products, enabling it to identify packaging issues such as incorrect component placement or incomplete packaging. After processing the captured image, the system classifies the package as either acceptable or defective and provides immediate results, allowing defective products to be identified and removed from the production line. By performing inference directly on the Raspberry Pi, the system offers a low-cost, portable, and efficient edge-computing solution that minimizes dependence on high-performance hardware while ensuring real-time operation. The integration of Python, YOLO, OpenCV, and Raspberry Pi creates an intelligent automated inspection system that reduces human error, improves quality control, increases production efficiency, and supports the adoption of smart manufacturing practices in the food packaging industry.

---

## Keywords

Food Package Inspection, YOLO Object Detection, Raspberry Pi, Computer Vision,  Deep Learning, Quality Control Automation, Packaging Defect Detection, Real-Time Image Processing, Edge Computing, Smart Manufacturing.

---

## 1. Introduction

Food packaging plays a vital role in preserving product quality, ensuring food safety, and maintaining customer trust in the food manufacturing industry. Proper packaging protects food products from contamination, damage, and spoilage while providing important information such as branding, nutritional details, and expiration dates. As production volumes continue to increase, maintaining consistent packaging quality has become a significant challenge for manufacturers. Traditional inspection methods largely depend on manual visual checks, which are time-consuming, labor-intensive, and susceptible to human errors caused by fatigue and inconsistency. These limitations can result in defective products reaching consumers, leading to financial losses and reputational damage for companies.
Recent advancements in Artificial Intelligence (AI), Computer Vision, and Deep Learning have enabled the development of automated inspection systems capable of performing accurate and real-time quality assessment. Among these technologies, the YOLO (You Only Look Once) object detection algorithm has gained popularity due to its high detection accuracy and fast processing speed, making it suitable for industrial applications. By integrating YOLO with edge-computing platforms such as Raspberry Pi, it is possible to create cost-effective and portable inspection systems that can operate directly on production lines without requiring expensive computing infrastructure.
This project presents an AI-Based Food Package Inspection System using YOLO and Raspberry Pi. The proposed system utilizes a camera module to capture images of food packages and applies a trained YOLO model to detect packaging defects such as incorrect component placement or incomplete packaging. The system automatically classifies packages as acceptable or defective and provides immediate feedback, enabling rapid removal of faulty products from the production process. By automating quality control, the system aims to reduce human intervention, improve inspection accuracy, enhance production efficiency, and support the adoption of smart manufacturing practices in the food packaging industry.

---

## 2. Literature Review

Artificial Intelligence (AI) and Deep Learning have significantly improved automated inspection systems in the food industry. Traditional manual inspection methods are often slow, inconsistent, and prone to human error, creating the need for intelligent computer vision solutions.
Kagaya et al. (2014) demonstrated that Convolutional Neural Networks (CNNs) achieve higher accuracy in food image detection and recognition compared to traditional machine learning methods. Their work highlighted the effectiveness of deep learning for complex food-related image analysis.
Wang et al. (2021) proposed a deep learning-based food recognition and food safety detection system using YOLO and Siamese networks. Their research showed that AI models can accurately recognize food items and detect foreign objects, supporting automated quality inspection in the food industry.

Karabay et al. (2025) developed a large-scale food image dataset and evaluated YOLOv8 for food detection. The study demonstrated that YOLO-based models provide high accuracy and real-time performance, making them suitable for industrial inspection applications.
Dhake et al. (2025) explored real-time object detection using Raspberry Pi and YOLO. Their findings showed that edge computing enables low-cost, low-latency, and efficient object detection, making Raspberry Pi a practical platform for industrial automation and quality control systems.
Based on these studies, YOLO, OpenCV, and Raspberry Pi provides an effective solution for automated food package inspection. The proposed system aims to detect packaging defects such as incorrect component placement or incomplete packaging in real time, thereby improving quality control, reducing human error, and enhancing production efficiency.

---

## 3. Problem Statement
In the food packaging industry, maintaining packaging quality is essential to ensure product safety, customer satisfaction, and compliance with industry standards. Traditional inspection methods rely on manual observation, which can be slow, inconsistent, and prone to errors, especially in high-speed production environments. To address these challenges, there is a growing need for an automated system that can accurately detect packaging defects in real time and improve overall quality control.
1.	Manual food package inspection is inefficient and error-prone, as human operators may miss defects due to fatigue, inconsistency, and high production volumes, leading to quality issues and financial losses. 
2.	Packaging defects such as incorrect component placement or incomplete packaging require real-time detection, creating the need for an automated, accurate, and cost-effective inspection system. 
3.	This project proposes an AI-based solution using a camera, Raspberry Pi, and YOLO object detection, enabling real-time identification of correctly and incorrectly packaged food products to improve quality control and production efficiency. 


---

## 4. Objectives

The specific objectives of this research are:

1. To develop an automated food package inspection system capable of identifying whether a food product is packaged correctly or contains packaging defects. 
2. To implement the YOLO object detection algorithm for real-time detection and classification of packaging conditions, such as incorrect component placement or incomplete packaging. 
3. To integrate a camera module with a Raspberry Pi for capturing and processing images efficiently on an edge-computing platform. 
4. To improve inspection accuracy and reduce human intervention by replacing manual quality checks with an AI-powered computer vision system. 
5. To enhance production efficiency and quality control by enabling fast, reliable, and cost-effective detection of packaging defects in food manufacturing environments.

---

## 5. Methodology

### 5.1 Data Collection and Annotation
A custom dataset of food package images is collected from roboflow universe.The dataset was created using a combination of publicly available food image datasets from Roboflow Universe and manually collected images from online sources. We gathered images for each menu item, including burgers, fries, wraps, nuggets, beverages, and side dishes. To improve model generalization, images were collected from different angles, lighting conditions, backgrounds, and object positions. The collected images are annotated using Roboflow, where bounding boxes are drawn around the relevant package components and defects. Each annotation is assigned a class label to enable supervised learning during model training.
### 5.2 Dataset Preprocessing
The annotated dataset is preprocessed to improve model performance and robustness. Images are resized to a uniform resolution suitable for YOLOv8 training, and data augmentation techniques such as rotation, flipping, scaling, and brightness adjustment are applied. The dataset is then divided into training, validation, and testing sets to ensure proper model development and evaluation.
### 5.3 YOLOv8 Model Training and Evaluation
The preprocessed dataset is used to train the YOLOv8 object detection model. Transfer learning with pretrained weights is employed to reduce training time and improve detection accuracy. The trained model is evaluated using performance metrics such as Precision, Recall, F1-Score, and Mean Average Precision (mAP). Hyperparameter tuning is performed to obtain optimal detection results.
### 5.4 Real-Time Image Acquisition and Detection
A camera connected to the Raspberry Pi continuously captures images from the production line. OpenCV is used to acquire and process image frames, which are then passed to the trained YOLOv8 model. The model performs real-time object detection by identifying packaging components and detecting defects with corresponding confidence scores.
### 5.5 Package Verification and Defect Classification
The detected packaging features are compared against predefined quality standards. The system verifies the package completetion and incorrect order placement. Based on the verification results, each package is classified as either acceptable or defective, allowing faulty products to be identified immediately.
### 5.6 Dashboard and Alert Generation
The inspection results are displayed on a monitoring dashboard showing package status, detected defects, and confidence values. A green LED indicates a correctly packaged product, while a red LED and buzzer are activated when a defect is detected. This enables operators to take immediate corrective action.
### 5.7 Raspberry Pi Edge Deployment
The complete inspection system is deployed on a Raspberry Pi, allowing image processing and object detection to be performed locally. Edge deployment reduces latency, minimizes network dependency, lowers operational costs, and provides real-time inspection capabilities suitable for industrial environments.


---

