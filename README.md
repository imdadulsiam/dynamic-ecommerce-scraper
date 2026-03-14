# Dynamic E-Commerce Scraper (Playwright & Python)

## Overview
An automated web scraping pipeline designed to extract, sanitize, and format product data from dynamic, JavaScript-rendered e-commerce platforms. 

## Technical Stack
* **Language:** Python
* **Framework:** Playwright (Headless Mode)
* **Data Format:** JSON

## Features
* **Dynamic Content Handling:** Utilizes explicit waits (`wait_for_selector`) and `networkidle` states to ensure JavaScript-rendered DOM elements are fully loaded before extraction.
* **Data Sanitization:** Automatically cleans raw string outputs (stripping currency symbols and commas) and casts them into strict floating-point numeric types for immediate database integration.
* **Resilient Extraction:** Implements error handling for missing HTML nodes to prevent script failure on inconsistent web pages.

## AI-Assisted Development
This codebase was rapidly prototyped and optimized using Prompt Engineering and LLM-driven development methodologies (Vibe Coding), focusing on clean architecture and strict data validation.
