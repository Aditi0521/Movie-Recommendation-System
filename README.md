Movie Recommendation System
Overview
This Movie Recommendation System is designed to recommend movies to users based on their preferences and viewing history. The system uses collaborative filtering and content-based filtering techniques to provide personalized movie recommendations.

Features
User Authentication: Users can register, log in, and log out.
Movie Recommendations: Based on user preferences and viewing history.
History: Track users' viewing history.

Setup Instructions
1. Clone the Repository
First, clone the repository to your local machine using the following command:

Copy code
git clone https://github.com/Aditi0521/Movie-Recommendation-System.git

2. Install Dependencies
Navigate to the project directory and install the necessary dependencies. It's recommended to use a virtual environment.

cd Movie-Recommendation-System
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt


3. Prepare the Dataset
Step 3.1: Generate movie_dict.pkl and simi.pkl
You need to run the Jupyter notebook provided in the project to generate movie_dict.pkl and simi.pkl. Follow these steps:

Open the Jupyter notebook file
Run the cells in the notebook to generate movie_dict.pkl and simi.pkl.
Once generated, copy these files (movie_dict.pkl and simi.pkl) to the project directory.


4. Initialize the Database
Run the following command to initialize the database:

python -c "import database; database.create_db()"


5. Run the Application
To run the application, execute the following command:

streamlit run app.py


6. Using the Application
Register: Create a new account.
Login: Log in to your account.
Generate movie recommendations
View History: See your viewing history and get movie recommendations.
