console.log("Ajax request")



let fetchBtn = document.getElementById('fetchdata');
fetchBtn.addEventListener('click',buttonClickHandler)

function buttonClickHandler() {
    console.log('You have clicked the fetchBtn');
    //Instantiate an xhr object

    const xhr  = new XMLHttpRequest();

    //open the object

    xhr.open('GET','static/jay.txt',true);

    // What to do on progress
    xhr.onprogress = function(){
        console.log('on progress');
    }

    xhr.onreadystatechange = function(){
        console.log("ready state is",xhr.readyState);
    }
    // What to do when response is ready

    xhr.onload = function(){

        console.log(this.responseText)
        return this.response().JSON(['message',this.responseText])

     
    }
    xhr.send();

    console.log('We are done')
}


let popBtn = document.getElementById('popBtn');
popBtn.addEventListener('click',popHandler);

function popHandler(){
    console.log('You have clicked the popHandler');
    //Instantiate an xhr object

    const xhr  = new XMLHttpRequest();

    //open the object

    xhr.open('GET','https://dummy.restapiexample.com/api/v1/employees',true);

    // What to do on progress
    // xhr.onprogress = function(){
    //     console.log('on progress');
    // }

    // xhr.onreadystatechange = function(){
    //     console.log("ready state is",xhr.readyState);
    // }
    // What to do when response is ready

    xhr.onload = function(){
        if(this.status === 200){
            let obj = JSON.parse(this.responseText);
            console.log(obj);
            let list = document.getElementById('list');
            str = "";
            obj.data.map((data)=>{
                console.log(data.employee_name)
                str += `<li>${data.employee_name}</li>`;
           })
            
            list.innerHTML = str;

        }
        else{
            console.log(this.responseText)
        }

    }
    xhr.send();

    console.log('We are done')
}

let Change = document.getElementById('Change');
Change.addEventListener('click',chngHandler);

function chngHandler(){
    
    const xhr = new XMLHttpRequest();
    xhr.open('GET','static/text.txt',true);

   
    xhr.onload = function(){

       document.getElementById("reqst").innerHTML = this.responseText;
       
    }

     xhr.send()

}
