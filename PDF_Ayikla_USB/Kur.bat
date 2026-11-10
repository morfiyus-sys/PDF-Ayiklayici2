@echo off
setlocal

set "EXE=%~dp0PDF_Ayikla.exe"

if not exist "%EXE%" (
    echo.
    echo HATA: PDF_Ayikla.exe bulunamadi.
    echo.
    pause
    exit /b 1
)

reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDFSayfaAyikla" /ve /d "PDF AYIKLA" /f >nul

reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDFSayfaAyikla" /v "Icon" /d "%EXE%" /f >nul

reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDFSayfaAyikla\command" /ve /d "\"%EXE%\" \"%%1\"" /f >nul

echo.
echo ==========================================
echo   PDF SAYFALARINI AYIKLA AKTIF
echo ==========================================
echo.
echo Artik PDF dosyasina sag tiklayabilirsiniz.
echo.
echo   PDF Sayfalarini Ayikla
echo.
echo secenegi kullanilabilir.
echo.
pause
