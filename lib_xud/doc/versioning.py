import os
from mako.template import Template
import argparse

def build_template(versions=None, destFolder=None, outputFile=None):

    # Description
    #
    # This program takes either a list of strings or a directory as an argument.  In the case of a directory it simply extracts a list of
    # immediate sub-directories, to use in place of the list of strings.
    # The purpose is that we store versions of the html documentation in different folders and each sub-dir is a containing folder.
    # We use mako to complete a template to generate a new html file to include in the Sphinx build (included in the conf.py file)
    # This template includes the javascript that navigates through the versions.
    # outputFileName is the resulting path/file of the versioning.html file.  Note that this appears in conf.py, so don't change it unless
    # you do so in both places!

    # Sample usage
    #build_template(versions=("1","2"))
    #build_template(destFolder="C:/Users/andrewdewhurst/Documents/temp/Explore_HW_Manual/html")


    # -- Define the template ---------------------------------------------------------
    raw_template = """
    <select name="version" id="version-select" value="Latest" onchange="changeVersion(this.value)" >
    <option selected disabled>Other versions</option>
    %for version in versions:
    <option value="html/${version}/">${version}</option>
    %endfor
    </select>

    <script>
    function changeVersion(val) {
        var loc = window.location.toString();
        var i = loc.indexOf("html/");
        if (i >= 0) {
            var s1 = loc.substring(0, i);
            var i2 = loc.indexOf("/", i+6)
            var s2 = loc.substring(i2+1);
            nl=s1.concat(val, s2);


            var request = new XMLHttpRequest();  
            request.open('GET', nl, true);
            request.onreadystatechange = function(){
            if (request.readyState === 4){
                if (request.status === 404) {  
                    alert("Oh no, it does not exist!");
                    window.location.assign(loc);
                    location.reload();
                }
                else {
                    window.location.assign(nl);
                }  
            }
        };
        request.send();    
        }
    }
    </script>"""

    # -- Now fill in the template to create a new html file ---------------------------------------------------------
    #Check if a list is provided, and always append "latest" so any version can navigate to the latest future version
    if destFolder==None:
        versions = list(versions)
        versions.append("latest")
    else:
        versions = []
        for f in os.listdir(destFolder):
            if os.path.isdir(destFolder + "/" + f):
                versions.append(f)
        versions.append("latest")

    #Use mako to process the template
    mytemplate = Template(filename='./versioning_template.html')
    mytemplate = Template(raw_template)
    filledTemplate = mytemplate.render(versions=(versions))

    #Create a file
    if outputFile == None:
        outputFile = "./_templates/versioning.html" # Default name and location.
    f= open(outputFile,"w+")

    #Write template data to the file created
    f.write(filledTemplate)

    #Close file
    f.close()




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help='path to html output folder')
    parser.add_argument("-v", nargs='+', help='comma sepearetd list of versions as strings, e.g. -v "v1", "v2", "v3"')
    parser.add_argument("-o", help='optional path and filename of the resulting html file.  Default is ./_temapltes/versioning.html')
    args = parser.parse_args()
    build_template(versions=args.v, destFolder=args.p, outputFile=args.o)



