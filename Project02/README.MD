
# CS 1XA3 Project02 - yangf51
## Overview 
This webpage is Frank Yang's custom CV, containing his resume, brief description about him, as well as a contact form that can email him.
## Custom Javascript Code 
Javascript was used for several key features of the website:
1. Animations
- These were all done using the AOS library, [https://michalsnik.github.io/aos/](https://michalsnik.github.io/aos/)
- This code provides smoother animations for the ```div``` on the homepage. Importantly, AOS must be initialized within the body of the code
```
<script>

//init AOS

AOS.init();

</script>
```
2. Small menu button
- This was a simple function that opens the small menu with the class w3-show and w3-hide. The code was altered from the w3 css template demo 21
```
function  myFunction() {

	var  x = document.getElementById("navDemo");

	if (x.className.indexOf("w3-show") == -1) {

		x.className += " w3-show";

	} else {

		x.className = x.className.replace(" w3-show", "");

	}

}
```
3. Day/Night Mode on the Homepage
- This code was written by myself, it attaches classes to the main ```<div>``` tags of the page, changing it's colour depending on the current colour
```
<script>

$(document).ready(function(){
	
	$("#day").click(function(){
		
		if($("div").hasClass("w3-light-grey")){

		$("div").addClass("w3-black")

		$("div").removeClass("w3-light-grey")

		$("#day").addClass("w3-blue")

		$("#day").removeClass("w3-black")

	} else  if ($("div").hasClass("w3-black")){
		
		$("div").addClass("w3-light-grey")

		$("div").removeClass("w3-black")

		$("#day").addClass("w3-blue")

		$("#day").removeClass("w3-light-grey")

		$("#about").removeClass("w3-light-grey")

        $("#nav").removeClass("w3-light-grey")
        $("#nav").addClass("w3-blue")

        $("#navDemo").removeClass("w3-light-grey")
        $("#navDemo").addClass("w3-blue")
    

	}

	});

});

</script>
```
4. Showing/Hiding DOM in the resume page
- This code was written by myself with reference to the jquery api, [https://api.jquery.com/toggle/](https://api.jquery.com/toggle/).
- This code attaches classes and toggles showing and hiding depending on the div clicked
- This code also changes hover effects depending on the current state of the div, when open there will be no hover effects, when closed it will have hover effects - giving it a button feel
- For space, one of the three div buttons is shown below:
```
<script>

$(document).ready(function(){

$(".exp").hide();

$("#experiences").click(function(){

$(".exp").toggle(100, function(){

if($(this).is(":visible")){
	
		$("#experiences").removeClass("w3-hover-opacity")

	} else{

		$("#experiences").addClass("w3-hover-opacity")

	}

	});

});

});

</script>
```
## Design Choices -
 
Several design choices were made for the webpage:
- Home Page
	- The home page was modeled after modern designs of being able to scroll down into content, with animations to keep the reader engaged. A standard 'call to action button' in the middle clearly indicate the most important information - the resume, and allow viewers to quickly navigate to it. 
- About Me
	- The about me sections show off the ability to jump to bookmarks using HTML, the smooth transition matches with the speed of the rest of the animations, showing continuity.
	- About me quickly shows the basic information about me, as well as my attitude towards work in a brief paragraph
- Resume
	- The resume page is the most important page, with the majority of my information
	- The information is made digestible through a card look, dividing sections
	- Not too much information is shown at the beginning to not overwhelm the reader. Instead they slowly click the cards and reveal more, making the information more digestible
- Contact Me
	- The contact me section is a quick way to be able to contact me, writing a form and sending a email. 
	- Importantly it also provides the most important information about me, without having to search through the resume section for it
- Colour Theme:
	-	The colour blue was chosen as it is my favourite colour
	-	Blue is also the colour of calmness, which is a good attitude to have while reading through the page

 
## References -
- w3 Templates HTML:
	- [https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_cv&stacked=h](https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_cv&stacked=h)
	- [https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_interior_design&stacked=h](https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_interior_design&stacked=h)
- w3.css:
	- [https://www.w3schools.com/w3css/4/w3.css](https://www.w3schools.com/w3css/4/w3.css)
- Javascript AOS Library:
	- [https://michalsnik.github.io/aos/](https://michalsnik.github.io/aos/)
- JQuery API
	- [https://michalsnik.github.io/aos/](https://michalsnik.github.io/aos/)

