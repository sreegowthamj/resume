# Resume

[![CircleCI](https://circleci.com/gh/sreegowthamj/resume.svg?style=svg)](https://circleci.com/gh/sreegowthamj/resume)

This project builds my personal résumé as HTML and PDF documents from 
reStructuredText. Download the latest build of my résumé from [releases](https://github.com/sreegowthamj/resume/releases/latest), or see 
[below](#getting-started) for instructions on building from source.

## Getting Started

These instructions will get you a copy of this project setup on your local 
machine for development and building purposes. 

### Supported Platforms

- macOS
- Linux

### Prerequisites

- Python 2.7 and Pip
- Make
- Google Chrome (If using Chromium, see [Specifying a Chrome Path])
- Aspell

### Steps

1. Clone the Repository 
    ```
    $ git clone https://github.com/sreegowthamj/resume.git
    ```
2. Change directories 
    ```
    $ cd resume
    ```
3. Install dependencies and build résumé documents
    ```
    $ make
    ```
4. Should built résumé documents
    ```
    $ ls -la dist
    ```

### Additional Make Targets

- `make` - Generate HTML and PDF documents output to `$BUILD_DIR`
- `make html` - Generate HTML document and open HTML for viewing
- `make pdf` - Generate both HTML and PDF documents and open PDF for viewing 
- `make requirements` - Install Python requirements from requirements.txt
- `make clean` - Remove all untracked/ignored files (including `dist`)

### Environment Variables

These environment variables are used within the Makefile and the bin/chrome 
script: 

- `BUILD_DIR` - Directory for built résumés. Default: `dist`
- `RESUME_NAME` - Filename (without extension) used for built résumés. Default: `Connor_McKelvey__Resume`
- `RESUME_SRC` - Résumé source file (must be reStructuredText). Default: `RESUME.rst`
- `CHROME_PATH` - Path to Chrome executable. Default depends on platform. See [Specifying a Chrome Path].

#### Specifying a Chrome Path

If [bin/chrome](bin/chrome) does not correctly identify the Chrome executable 
for your platform or if you would like to use [Chromium](https://www.chromium.org/) 
instead, you can override the path to the executable with an environment variable. 

`CHROME_PATH=</path/to/chrome> make`

## Releasing

HTML and PDF résumé documents are automatically built on every commit using 
[CircleCI](http://circleci.com/). Résumé documents from tagged commits (e.g. v1.1.2) 
are uploaded to this project's [Releases](https://github.com/sreegowthamj/resume/releases) 
page.

## Built With

- [Docutils](http://docutils.sourceforge.net/) - reStructuredText to HTML conversion
- [Libsaas](https://github.com/sass/libsass-python) - Scss preprocessing
- [Make](https://www.gnu.org/software/make/) - Dependency installation and résumé generation
- [Chrome](https://www.google.com/chrome/) - HTML to PDF conversion
- [GHR](https://github.com/tcnksm/ghr) - Résumé uploading

## License

This project is not a library and is purpose built for my needs, feel free to 
fork this repository and adapt it for your own. This project is licensed under 
the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## TODO

- Automated layout testing using Galen Framework

[Specifying a Chrome Path]: #specifying-a-chrome-path
