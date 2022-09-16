# Getting your Tinder auth token
> This code seems to change `once` every day. \
> I have not yet looked into the automation of getting this token at this time.

## Process
* In the browser of your choosing, head to https://tinder.com/. 
* Before logging in, open developer options in your browser and navigate to the `network` tab. 
 ![image](https://user-images.githubusercontent.com/76274780/190454755-23cdd2e7-0137-47dd-99ea-254e69917693.png) 
* Proceed with the login process. 
* Once you have fully logged in, search for `https://api.gotinder.com/v2/recs/core?locale=en` in the `filter` search box in developer options. \
 ![image](https://user-images.githubusercontent.com/76274780/190454884-c7828fa5-f632-4016-9879-8c3296879d35.png)  
* This should filter out all unnecessary files and you should be left with a handful of files titles `core?local=en`. 
 ![image](https://user-images.githubusercontent.com/76274780/190454997-fef35890-4b57-487c-b129-082916c96198.png) 
* **IMPORTANT** - If you do not see any ‘core?local=en’ files, you will need to click around more on the Tinder site. I can’t seem to find the direct trigger for this file showing up. 
* There will be different versions of 'core?local=en'. 
* Clicking through the different 'core?local=en' files look at the `Headers` tab of each file. You will want to find a `GET` Request Method version of the file which can be seen in the `General Section` as seen in the images below. 
* Any GET version of this file should have the token we are searching for. 
 ![image](https://user-images.githubusercontent.com/76274780/190456960-0d19b752-5a08-4bc1-a6cf-33ddc080118e.png) 
 ![image](https://user-images.githubusercontent.com/76274780/190456984-f074f9f4-3669-4e6b-8938-4506ed72698d.png) 
* You will find 2 more 'sections' under the `general` section.  
 ![image](https://user-images.githubusercontent.com/76274780/190455807-66762e33-e15f-434e-b459-bbf936757aaa.png) 
* For sake of simplicity and understanding I have collapsed the three sections in the image above to show the 3 sections titles that I am referring to. 
* Each section contains a lot of information that isn't visible in the image. 
* In the `Request Headers` portion you will find a variable called `x-auth-token`. It should be the 2nd variable from the bottom. This is the token needed to use this library. 
* Your Auth Token will be in the format of `00000000-0000-0000-0000-000000000000`.
* **IMPORTANT** - Do NOT share this token with anyone. This is your profiles personal token and if anyone else gains access to this token they will have full access to your personal profile.