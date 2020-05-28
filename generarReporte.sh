#!/bin/bash

wkhtmltopdf --javascript-delay 8000 index.html reporte.pdf
xreader reporte
