# Charms
Charms is a required subject taught at Hogwarts School of Witchcraft and Wizardry, in which the students learn to perform different spells on objects or individuals. During the class, the professor Filius Flitwick created different challenges for the students to do in a certain amount of time. The main objective of this activity is to teach the students to perform a spell by following specific instructions and score as many points as they can for their corresponding houses.

### Team
* Renata Saldívar González
* Lorraine Bichara Assad

### Code Examples
```python
int i, j;

function void main()
{
  i = 1;
  j = 2;
  print(i+j);
}
```

```python
bool b;

function bool uno()
{
  return(5>4);
}

function void main()
{
  b = uno();
  if(b == False)
  {
    print("verdadero");
  }
  else
  {
    print("falso");
  }
}
```

```python
int i;
function void main()
{
  i = 1;
  while(i < 5)
  {
    print(hola);
    i = i + 1;
  }
}
```

### Requirements
Make sure you have the following tools:
* Python 3
* Django
* Bootstrap 3
* ANTLR

### Setup the project
1. Clone this repository into your local machine

```bash
$ git clone https://github.com/renata-sg/Charms
```

### Running the project
#### Using the GUI
1. Run the following commands to get ANTLR running:
```bash
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
$ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
$ antlr4 -Dlanguage=Python3 CharmsLexer.g4
$ antlr4 -Dlanguage=Python3 CharmsParser.g4
```
2. Make sure that CharmsProject/CharmsApp/views.py contains the correct paths to CharmsRunner.py and inputFile.txt (this file is in Downloads folder)

3. Navigate into CharmsProject and run:
```bash
$ python3 manage.py runserver
```
4. Open http://localhost:8000/ in your web browser
5. Choose a spell from the list or create your own program by dragging the different blocks onto the canvas.
6. Click on "Compile code" to generate inputFile.txt. This file contains a program written in Charms that can be executed, and it will be automatically downloaded into your Downloads folder.
7. Click on "Execute code" to run the code you created.

#### Using the console
1. Create a .txt file with a sample program.
2. Run:
```bash
$ python3 CharmsRunner.py *your input file here*
```

### Troubleshooting
* Make sure that CharmsProject/CharmsApp/views.py contains the correct paths for the CharmsRunner.py file to execute and the inputFile.txt.
* Run all ANTLR commands before starting.
* Run the project in a new tab/window.

### Tips
For best results, run the project using Google Chrome not on incognito and download the following extensions:
* [Downloads Overwrite Already Existing Files](https://chrome.google.com/webstore/detail/downloads-overwrite-alrea/lddjgfpjnifpeondafidennlcfagekbp)
* [Disable Download Bar](https://chrome.google.com/webstore/detail/disable-download-bar/gjdldigdojpjlmphnogmcmhojfadfmem?hl=en-GB)