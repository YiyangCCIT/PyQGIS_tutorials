@echo off
SET cur_dir=%cd%
SET qgis_dir=C:\Program Files\QGIS 3.10\bin

cd %qgis_dir%

call o4w_env.bat
call py3_env.bat
call qt5_env.bat

path %OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%

cd %cur_dir%

"%PYTHONHOME%\Scripts\pyuic5.bat" -x main.ui -o main.py

