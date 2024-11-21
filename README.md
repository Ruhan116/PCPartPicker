# PCPartPicker  

**PCPartPicker** is a desktop application designed to assist PC enthusiasts in creating custom computer builds effortlessly. By combining an intuitive frontend, a robust backend, and efficient web scraping capabilities, this project streamlines the process of selecting, verifying, and saving compatible PC components.  

---

## Screeshots

### Login-Page
![Screenshot 2024-11-21 112410](https://github.com/user-attachments/assets/c5b58351-8bb6-4b69-b63e-4711470c2443)
### Signup-Page
![Screenshot 2024-11-21 112425](https://github.com/user-attachments/assets/2654f10c-f99d-420c-941a-fde901e99825)
### Landing-Page
![Screenshot 2024-11-21 112529](https://github.com/user-attachments/assets/ab851096-3f35-4d27-a017-1d56c2558956)
### Choosing Parts Page
![Screenshot 2024-11-21 112542](https://github.com/user-attachments/assets/a4250abd-4461-4b55-964e-01deb903742b)
### Component Details page (CPU)
![Screenshot 2024-11-21 112556](https://github.com/user-attachments/assets/f3f74945-6dc9-4996-a08c-0830ad1e060f)
### Component Details Page (HDD)
![Screenshot 2024-11-21 112612](https://github.com/user-attachments/assets/ab24fb5b-b9a2-42c3-a775-2f0c478864e7)

## Features  

- **Frontend**: Built with **PyQt6**, offering a responsive and user-friendly interface.  
- **Database**: Uses **SQLite** for efficient data management of PC components, builds, and user preferences.  
- **Web Scraping**: Employs **Beautiful Soup** to fetch real-time data from online sources, ensuring accurate and updated information on PC parts.  
- **Compatibility Checker**: Ensures that selected components are compatible with each other, minimizing the risk of hardware mismatches.  
- **Search and Filter Options**: Allows users to search components by specifications, brand, and price, enabling tailored builds.  
- **Build Saving**: Offers the ability to save and revisit custom builds for future reference.

---

## Tech Stack  

- **Python**  
  - **PyQt6**: For building the graphical user interface.  
  - **SQLite**: For lightweight and reliable database management.  
  - **Beautiful Soup**: For web scraping and data collection.  

---

## Current Progress  

### 1. Frontend Development  
- Basic UI structure created with PyQt6, enabling initial navigation between pages.  
- Work on component selection screens and compatibility result display is underway.  

### 2. Backend Integration  
- SQLite database schema initialized for storing part information and saved builds.  
- Development of methods for CRUD (Create, Read, Update, Delete) operations is ongoing.  

### 3. Web Scraping  
- Web scraping scripts implemented using Beautiful Soup to collect data from multiple online retailers.  
- Focus on refining data extraction to ensure accuracy and relevance.

### 4. Core Features  
- Initial implementation of compatibility logic for common PC components (CPU, motherboard, RAM, etc.).  
- Planning for search filters and saving builds has been outlined.

---

## Getting Started  

### Prerequisites  
- Python 3.8 or higher  
- PyQt6  
- Beautiful Soup 4  
- SQLite  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/Ruhan116/PCPartPicker.git  
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd PCPartPicker  
   ```  
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. Run the application:  
   ```bash  
   python main.py  
   ```  

---

## Future Goals  

- Expand compatibility checker to include a broader range of hardware.  
- Add support for user accounts and build history.  
- Integrate price tracking and alerts for selected components.  
- Polish UI for a more interactive and visually appealing experience.

---
