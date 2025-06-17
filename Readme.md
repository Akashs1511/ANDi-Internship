# Doctor Appointment Booking System

## Overview
The Doctor Appointment Booking System is a Python-based console application designed to streamline appointment management, prescription writing, and patient record-keeping for healthcare professionals. This project leverages `pandas` for data management and provides a modular, beginner-friendly implementation suitable for small-scale medical practices.

## Features
- **Appointment Management**: Easily book and manage patient appointments via a console-based dashboard.
- **Prescription Writing**: Write prescriptions by selecting drugs and dosages, with support for pre-filled treatment templates.
- **Drug Management**: Organize drugs by type for quick access during prescription creation.
- **Patient History**: Patients can view their appointment and prescription history.
- **Invoicing**: Generate basic invoices based on appointment records.
- **Data Persistence**: Uses CSV files (`appointments.csv`, `prescriptions.csv`, `drugs.csv`, `treatments.csv`) for storing data.

## Requirements
- Python 3.6 or higher
- `pandas` library

## Installation
1. **Clone or Download the Project**  
   Download the project files or clone the repository to your local machine.

2. **Install Dependencies**  
   Ensure you have Python installed. Then, install the required `pandas` library using pip:
   ```bash
   pip install pandas
   ```

3. **Verify Setup**  
   Ensure the following files are created automatically on first run: `appointments.csv`, `prescriptions.csv`, `drugs.csv`, and `treatments.csv`.

## Usage
1. **Run the Application**  
   Navigate to the project directory and run the script:
   ```bash
   python doctor_system.py
   ```

2. **Interact with the Menu**  
   The application provides a console-based menu with the following options:
   - **Book Appointment**: Schedule a new appointment for a patient.
   - **Write Prescription**: Create a prescription by selecting a drug and dosage.
   - **Use Treatment Template**: Apply a pre-filled treatment template for quick prescriptions.
   - **Generate Invoice**: View a basic invoice for a patient.
   - **Patient History**: Check a patient's appointment and prescription history.
   - **Exit**: Close the application.

3. **Example Workflow**  
   - Select "1" to book an appointment for a patient (e.g., "John Doe" on "2025-06-17" at "10:00").
   - Select "2" to write a prescription, choosing a drug type (e.g., "Painkiller") and drug (e.g., "Ibuprofen").
   - Select "5" to view the patient's history.

## Project Structure
- `doctor_system.py`: Main script containing the application logic.
- `appointments.csv`: Stores appointment data.
- `prescriptions.csv`: Stores prescription records.
- `drugs.csv`: Stores drug information, categorized by type.
- `treatments.csv`: Stores pre-filled treatment templates.

## Future Improvements
- Add a graphical user interface (GUI) using `tkinter` or a web interface using `Flask`.
- Replace CSV storage with a proper database like SQLite.
- Implement user authentication for doctors and patients.
- Add analytics features, such as visualizing prescription trends using `matplotlib`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please contact me at [akash02155@gmail.com].
