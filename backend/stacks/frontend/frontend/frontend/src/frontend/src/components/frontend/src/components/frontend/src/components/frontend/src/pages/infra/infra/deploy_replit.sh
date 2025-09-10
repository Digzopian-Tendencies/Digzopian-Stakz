#!/bin/bash
npm install
pip install -r backend/requirements.txt
npm run dev --prefix frontend
