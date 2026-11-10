@echo off

reg delete "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDFSayfaAyikla" /f >nul 2>&1

echo.
echo ==========================================
echo   PDF SAYFALARINI AYIKLA KALDIRILDI
echo ==========================================
echo.
pause
