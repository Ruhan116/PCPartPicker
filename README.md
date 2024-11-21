# PCPartPicker  

**PCPartPicker** is a desktop application designed to assist PC enthusiasts in creating custom computer builds effortlessly. By combining an intuitive frontend, a robust backend, and efficient web scraping capabilities, this project streamlines the process of selecting, verifying, and saving compatible PC components.  

---

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
