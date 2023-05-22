# Stori QA Automation Challenge

_Prueba tecnica para QA Automation en Stori Card_


## Tecnologias ⌨️
1. Python. (3.9)
2. Selenium.
3. Web Driver.

## Clona el repositorio 📦

```
git clone https://github.com/josbp0107/stori-qa-automation-challenge.git
```
```
cd stori-qa-automation-challenge
```

### Instalar modulos en un entorno virtual 🔧

#### Linux & Mac

```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip3 install -r requirements.txt
```

#### Windows
```
py -m venv venv
```
```
venv\Scrips\activate
```
```
pip install -r requirements.txt
```

### Archivos requeridos 📋

#### Web Driver

1. Debes descargar los siguientes drivers para poder ejecutar la automatizacion correctamente

   * Chrome: https://chromedriver.chromium.org/downloads
   * Firefox: https://github.com/mozilla/geckodriver/releases
   * Microsoft Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   
2. Luego de haber descargado el driver, debes crear una carpeta en la raiz con el nombre drivers
3. Y finalmente, dentro de esta carpeta debes agrega los drivers de cada navegador.

**Recuerda tener actualizado el navegador en la ultima versión**

### Como ejecutar el proyecto 🚀
1. Ubicate en la raiz del proyecto stori-qa-automation-challenge
2. Para ejecutarlo en un navegador especifico (Chrome, Firefox o Edge), debes agregar la flag ``--browser``
   * Google Chrome:
   
      ``` py .\main.py --browser chrome ```
   * Firefox:
   
      ``` py main.py --browser firefox ```
   
   * Microsoft Edge: 
   
     ``` py main.py --browser edge ```
3. Simplemente espera que se ejecuten todos los Test y puedes validar el resultado de cada test en el archivo de ``report.html`` que se encuentra en la carpeta de **Reports**


⌨️ con ❤️ por [Jose Ballesteros Paternina](https://github.com/josbp0107) 😊
