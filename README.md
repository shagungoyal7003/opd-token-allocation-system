# OPT_TOKEN - OPD Token Allocation System

This project implements a smart OPD token allocation system using Flask API with priority-based scheduling and emergency patient handling.

## Features

- Doctor Management
- Slot Creation
- Token Booking
- Emergency Priority Handling
- Waiting List Management
- Automatic Reallocation on Cancellation

## Tech Stack

- Python
- Flask
- REST API

## Priority Order

| Type | Priority |
Emergency | 4
Paid Priority | 3
Follow-up | 2
Normal | 1

## Project Files

- app.py → Main Flask Server
- API DESIGN.txt → API Endpoints Design
- Token allocation algorithm.txt → Allocation Logic
- Documentation.txt → Edge Case Handling
- OPD DAY SIMULATION.txt → Working Simulation

## ▶ How To Run

1. Install Flask
pip install flask

2.Run Server
python app.py

3.Open browser
http://127.0.0.1:5000

4.Output
Server starts successfully and supports booking, cancellation and emergency insertion.

5.OPD Token System Running
Developed for OPT_TOKEN Assignment












