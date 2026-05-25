import os

if __name__ == "__main__":
    """
    Launches the professional fact checker cleanly from the root workspace directory.
    Execution: python main.py
    """
    print("Launching the Advanced Fact-Checking RAG Application...")
    os.system("streamlit run ui/app.py")