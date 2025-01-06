 let messageTxt = document.querySelector('.output-message');
 /*
 *innerHTML
 *respects the HTML structure and returns the raw content inside the element.
 */
 console.log(messageTxt.innerHTML);
  /*
 *innerText
 *reflects the visible text only, ignoring elements that are hidden (display: none, visibility: hidden, or off-screen).
 */
 console.log(messageTxt.innerText); 

 function chooseLunch (element){
    const selectedOption = element.options[element.selectedIndex];
 }