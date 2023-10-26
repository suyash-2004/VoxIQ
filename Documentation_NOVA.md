# NOVA - Neuro Optimized Virtual Assistant

## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Overview](#11-overview)
  - [1.2 Purpose](#12-purpose)
- [2. Features](#2-features)
  - [2.1 Speech Recognition](#21-speech-recognition)
  - [2.2 Voice Synthesis](#22-voice-synthesis)
  - [2.3 Greeting and Time-Based Interaction](#23-greeting-and-time-based-interaction)
  - [2.4 Command Input](#24-command-input)
  - [2.5 Wikipedia Search](#25-wikipedia-search)
  - [2.6 File and Text File Handling](#26-file-and-text-file-handling)
  - [2.7 Web Search](#27-web-search)
  - [2.8 Timer](#28-timer)
  - [2.9 Music Player](#29-music-player)
  - [2.10 Navigation](#210-navigation)
- [3. Usage](#3-usage)
- [4. Dependencies](#4-dependencies)
- [5. Performance](#5-performance)
- [6. Conclusion](#6-conclusion)

## 1. Introduction

### 1.1 Overview

NOVA, which stands for "Neuro Optimized Virtual Assistant," is a Python-based virtual assistant designed to assist users in performing various tasks through voice commands. It leverages several technologies and libraries, including speech recognition, voice synthesis, and web APIs, to provide an interactive and helpful experience.

### 1.2 Purpose

The purpose of NOVA is to serve as a desktop assistant that can perform a wide range of tasks, from answering questions and retrieving information from the web to managing files and playing music. Users can interact with NOVA by speaking commands, and it responds both verbally and through actions.

## 2. Features

NOVA boasts a variety of features that make it a versatile virtual assistant:

### 2.1 Speech Recognition

NOVA utilizes the SpeechRecognition library to recognize and interpret user voice commands. Users can communicate with NOVA by speaking naturally, and the assistant processes these commands to perform the requested actions.

<img width="554" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/fdbc6b60-e440-4b2d-88aa-b731ff755770" align="center">

### 2.2 Voice Synthesis

The assistant employs the pyttsx3 library for voice synthesis. It can respond to user queries by speaking out the results or providing information.

<img width="554" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/8639897e-7016-4652-ac8f-23d41dee5d97" align="center">

### 2.3 Greeting and Time-Based Interaction

NOVA greets the user based on the time of day, offering a personalized experience with messages such as "Good Morning" or "Good Evening." It makes the interaction with the virtual assistant more engaging.

<img width="482" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/0f31e9f0-dd4d-4320-a573-b63b07cc56d2" align="center">

### 2.4 Command Input

Users can initiate interactions with NOVA by simply speaking. The assistant listens for voice commands and responds accordingly.

<img width="447" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/134b84f3-285b-4121-a4c9-c20aab54e7f6"  align="center">

### 2.5 Wikipedia Search

NOVA can perform Wikipedia searches to provide users with information on various topics. It fetches summarized content from Wikipedia and reads it aloud to the user.

<img width="509" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/eedda3fd-b776-4894-ab9d-3be605eb5aa9" align="center">

### 2.6 File and Text File Handling

Users can instruct NOVA to open text files. The assistant can locate and read the contents of specified text files.

<img width="667" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/b7dc244d-dcbe-462c-9e79-5b06bb0f70fd" align="center">

### 2.7 Web Search

NOVA is capable of performing web searches using the pywhatkit library. Users can ask NOVA to search for information on a specific topic, and it will open a web browser to display the search results.

<img width="485" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/fdbc6b60-e440-4b2d-88aa-b731ff755770" align="center">

### 2.8 Timer

NOVA can set timers for specified durations, whether in seconds, minutes, or hours. It provides alerts and notifies users when the set time is up.

![Uploading Doc1_cropped_pages-to-jpg-0001.jpg…]()


### 2.9 Music Player

The assistant can play music from a predefined directory. Users can ask NOVA to start playing music, and it selects a random song to play.

<img width="698" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/e1827734-48c6-4143-8726-c35106cc5aee" align="center">

### 2.10 Navigation

NOVA can assist users with navigation by providing directions to a specified destination. It opens Google Maps with the destination pre-filled for easy access.

<img width="361" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/79edc848-9e9c-4a44-a7a9-bb6ae7ed80fd" align="center">

<img width="596" alt="image" src="https://github.com/suyash-2004/NOVA/assets/61971096/eeb2649c-9258-405f-ba38-e1e2931a27a5" align="center">


## 3. Usage

Users can interact with NOVA by speaking voice commands. The assistant will listen and interpret the commands, then take appropriate actions based on the request. Users can ask questions, request information, open files, set timers, play music, and more.

## 4. Dependencies

NOVA relies on several libraries and APIs, including:

- speech_recognition
- pyttsx3
- wikipedia
- pywhatkit
- tqdm
- webbrowser

## 5. Performance

NOVA performs well for various tasks, including voice recognition and synthesis. However, its performance may vary based on the user's hardware and network conditions, especially when making web searches or playing music.

## 6. Conclusion

NOVA, the Neuro Optimized Virtual Assistant, is a versatile Python-based desktop assistant designed to assist users in performing a wide range of tasks through voice commands. With features such as speech recognition, web searches, timer management, and more, NOVA aims to enhance the user's desktop experience by providing helpful and interactive assistance.

Please note that this is a basic outline, and you can expand on each section with more details, instructions, and examples. Additionally, you may want to include information about installation and any future development plans for your virtual assistant.
