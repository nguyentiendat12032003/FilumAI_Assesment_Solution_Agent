# FilumAI Assessment Solution Agent

## 📋 Project Description

This is a simple AI agent system designed to analyze user pain points and suggest appropriate solutions from a list of available features. The system uses TF-IDF algorithm and cosine similarity to find the most suitable features.

## 🏗️ Project Structure

```
FilumAI_Assesment_Solution_Agent/
├── main.py                 # Main file to run the entire system
├── requirements.txt        # List of required Python libraries
├── README.md              # This guide file
├── .gitignore             # Git exclusion file
├── venv/                  # Python virtual environment directory
├── data/                  # Data directory
│   ├── input_user.json    # User input data
│   └── features.json      # List of features and descriptions
├── agent/                 # AI agent processing module
│   └── agent_tfidf.py    # TF-IDF algorithm for analysis and suggestions
├── user/                  # User input processing module
│   └── user_input.py     # User input handling
└── log/                   # Logging module
    ├── log.py            # Activity logging
    └── matching_log.json # Matching result log file
```

## 🚀 Local Setup Guide

### Step 1: Environment Setup

1. **Create Python virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Run Application

1. **Run the entire system:**
   ```bash
   python main.py
   ```

2. **Or run individual modules:**
   ```bash
   # Input pain point from user
   python user/user_input.py
   
   # Analyze and suggest solutions
   python agent/agent_tfidf.py
   
   # Log activities
   python log/log.py
   ```

### Step 3: Using the Application

When you run `python main.py`, the system will:

1. **Prompt for input:** The system will ask you to enter your pain point
2. **Process your input:** Your pain point will be saved to `data/input_user.json`
3. **Analyze and suggest:** The AI agent will analyze your pain point and suggest the most suitable feature
4. **Display results:** You'll see the suggested solution with explanation
5. **Log activities:** All matching activities are logged for future analysis

**Example usage:**
```bash
$ python main.py
Nhập pain point của bạn: I need help with customer support overload
✅ Pain point đã được lưu vào data/input_user.json
- Pain Point: "I need help with customer support overload"
  - Suggested Solution: "AI Inbox (AI Customer Service)"
  - How it helps: Reduces agent workload by 30–50% through AI-driven answers
Log đã được lưu vào log/matching_log.json
```

## 📁 Python Files Explanation

### 1. `main.py`
- **Function:** Main file that orchestrates the entire system
- **Operation:** Runs 3 modules sequentially: user input → agent analysis → logging
- **Uses:** `subprocess.run()` to execute other Python scripts

### 2. `user/user_input.py`
- **Function:** Handles user input
- **Main features:**
  - Input pain point from console
  - Validate input data
  - Save to `data/input_user.json` file
- **Output data structure:**
  ```json
  {
    "pain_point": "user's problem description"
  }
  ```

### 3. `agent/agent_tfidf.py`
- **Function:** Analyzes pain point and suggests solutions
- **Algorithms used:**
  - **TF-IDF Vectorization:** Converts text to numerical vectors
  - **Cosine Similarity:** Calculates similarity between pain point and features
- **Processing workflow:**
  1. Load data from `features.json` and `input_user.json`
  2. Create corpus from feature descriptions, keywords, use cases
  3. Vectorize text using TF-IDF
  4. Calculate similarity scores
  5. Select feature with highest score
- **Output:** Prints suggestion results to console

### 4. `log/log.py`
- **Function:** Logs matching activities
- **Features:**
  - Calculate similarity scores for all features
  - Save timestamp, pain point, and matching results
  - Append to `log/matching_log.json` file
- **Log structure:**
  ```json
  {
    "timestamp": "2024-01-01T12:00:00",
    "pain_point": "problem description",
    "matches": [
      {
        "feature_name": "Feature name",
        "category": "Category",
        "score": 0.85
      }
    ]
  }
  ```

## 📊 Data

### `data/features.json`
Contains list of features with information:
- `feature_name`: Feature name
- `category`: Category (VoC, AI Customer Service, etc.)
- `description`: Detailed description
- `keywords`: Related keywords
- `use_cases`: Use cases
- `how_it_helps_examples`: Examples of how the feature helps
- `docs_link`: Documentation link

### `data/input_user.json`
Stores pain point entered by user.

### `log/matching_log.json`
Stores matching history for analysis and improvement.

## 🔧 Configuration and Customization

### Adding New Features
1. Add entry to `data/features.json`
2. Ensure all fields are complete: description, keywords, use_cases, how_it_helps_examples

### Adjusting Algorithm
- Change vectorizer in `agent/agent_tfidf.py`
- Add text preprocessing
- Use different similarity algorithms

## 🐛 Troubleshooting

### Common Errors:
1. **ModuleNotFoundError:** Run `pip install -r requirements.txt`
2. **FileNotFoundError:** Ensure JSON files exist in `data/` directory
3. **Encoding error:** Ensure JSON files use UTF-8 encoding

### Debug:
- Check logs in `log/matching_log.json`
- Run individual modules for debugging
- Print intermediate variables in code
