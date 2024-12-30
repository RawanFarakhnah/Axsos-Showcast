const tempreture = document.getElementById("temprature");

function convert(element) {
  let numberGroup1 = document.querySelectorAll(".num");
  let numberGroup2 = document.querySelectorAll(".num2");

  if(element == "fer")
  {
    for(let i = 0; i < numberGroup1.length ; i++)
    {
      numberGroup1[i].innerHTML = toFahrenheit(numberGroup1[i].innerHTML);
    }

    for(let i = 0; i < numberGroup2.length ; i++)
    {
       numberGroup2[i].innerHTML = toFahrenheit(numberGroup2[i].innerHTML);
    }
  }
  else if(element == "cel")
  {
    for(let i = 0; i < numberGroup1.length ; i++)
      {
        numberGroup1[i].innerHTML = toCelsius(numberGroup1[i].innerHTML);
      }
  
      for(let i = 0; i < numberGroup2.length ; i++)
      {
        numberGroup2[i].innerHTML = toCelsius(numberGroup2[i].innerHTML);
      }
  }
}



function toCelsius(fDegrees) {
  return Math.ceil((fDegrees - 32) * 5 / 9);
}

function toFahrenheit(cDegrees)
{
  return  Math.floor((9/5 * cDegrees) + 32);
}


const accept = document.getElementById("btn");

function policy(element) {
    const message = document.getElementById("del")
    message.remove( element);
}
