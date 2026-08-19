## Gemini AI Clone

A responsive AI chat application built with React.js, Context API, and the Google Gemini API. This project recreates the core experience of Gemini with a modern interface, chat history, prompt suggestions, loading animations, and AI-generated responses.

# Features
Responsive Gemini-inspired UI
Collapsible sidebar
Chat history
New Chat functionality
Interactive prompt suggestion cards
Fixed chat input
Enter-to-send functionality
Google Gemini API integration
AI-generated responses
Loading animation
Response formatting
React Context API for global state management
Responsive design for smaller screens
Technologies Used
React.js
Vite
JavaScript
CSS
Context API
Google Gemini API
@google/genai

# Project Structure
gemini-clone/
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── Sidebar/
│   │   │   ├── Sidebar.jsx
│   │   │   └── Sidebar.css
│   │   └── Main/
│   │       ├── Main.jsx
│   │       └── Main.css
│   ├── context/
│   │   └── Context.jsx
│   ├── config/
│   │   └── gemini.js
│   ├── App.jsx
│   ├── App.css
│   └── main.jsx
├── .env
├── .gitignore
├── index.html
├── package.json
└── vite.config.js

# How It Works
User
  ↓
React Chat Interface
  ↓
Context API
  ↓
Gemini Configuration
  ↓
Google Gemini API
  ↓
AI Generated Response
  ↓
React UI
Main Components
Sidebar

# The sidebar provides:

New Chat button
Collapsible navigation
Chat history
Settings section
Help section
Main Dashboard

# The dashboard includes:

Personalized greeting
Prompt suggestion cards
AI conversation area
User messages
AI responses
Loading animation
Context API

# The Context API manages global application state including:

Input prompt
Chat history
Loading state
AI response
Sidebar state
New chat functionality
Gemini API

The application uses Google's Gemini API through the @google/genai SDK to generate responses to user prompts.

Screens
Dashboard

The main screen provides prompt suggestions and a clean Gemini-inspired interface.

# Chat

Users can enter prompts and receive AI-generated responses.

# Sidebar

The collapsible sidebar keeps track of recent conversations.

# Learning Objectives

This project was developed to practice:

React component architecture
React Hooks
Context API
State management
API integration
Environment variables
Asynchronous JavaScript
Loading states
Responsive CSS
AI application development
Future Improvements
Persistent chat history using local storage
Multiple conversation sessions
Delete chat functionality
Markdown rendering
Dark mode
Voice input
Image upload
Streaming AI responses
Backend API for secure Gemini API integration
User authentication

# Disclaimer

This project is an educational Gemini-inspired clone created for learning purposes. It is not affiliated with or officially endorsed by Google.

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.
