const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')
console.log('inside review.js')
// text=event.target.text
// get the form, confirm-box and csrf token
const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    console.log(size)
    console.log(children.length)
    for (let i=0; i <= children.length; i++) {
        if(i <= size) {
            children[i+1].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            // one.classList.add('checked')
            // two.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }
        default: {
            handleStarSelect(0)
        }
    }

}

const getNumericValue = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } 
    else if (stringValue === 'second') {
        numericValue = 2
    }
    else if (stringValue === 'third') {
        numericValue = 3
    }
    else if (stringValue === 'fourth') {
        numericValue = 4
    }
    else if (stringValue === 'fifth') {
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue
}

if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
        // console.log(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        // value of the rating not numeric
        const val = event.target.id
        console.log(event.target.id)
        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            // product id
            const id = e.target.id
            // console.log(id)
            // value of the rating translated into numeric
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/shop/rate_product/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': id,
                    'val': val_num,
                    // 'review':
                },
                success: function(response){
                    // console.log(response)
                    confirmBox.innerHTML = `<h1>Successfully rated with ${response.score}</h1>`
                },
                error: function(error){
                    // console.log(error)
                    confirmBox.innerHTML = '<h1>Ups... something went wrong</h1>'
                }
            })
        })
    }))
}
const submit_review=document.getElementById('submit_review')
// const review_form = document.querySelector('.review-form')
const text = document.getElementById('review')
const prodID = document.getElementsByName('prodID')
// console.log(review_form)
console.log(text)
console.log(prodID)



// const csrf = document.getElementsByName('csrfmiddlewaretoken')
// $('#submit_review').click(function (event){
// $("#review_form").submit(function (e){
    // e.preventDefault();
$(document).on('submit','#review-form', function(e){
    e.preventDefault()

$.ajax({
    url : "/shop/review_product/",
    type : "POST", // http method
    data : {
        prodID:$('#prodID').val(),
        review:$('#review').val(),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() , //This is must for security in Django
    }, // data sent with the post request

    // handle a successful response
    success: function(response){
        // console.log(response)
        confirmBox.innerHTML = `<h1>Successfully reviewed , If you havent rated yet ,Please click on the star to rate it </h1>`
        return
    },
    error: function(error){
        // console.log(error)
        confirmBox.innerHTML = '<h1>Ups... something went wrong</h1>'
        return
    }
})

});


// console.log('hare')

// const one=document.getElementById('first')
// const two=document.getElementById('second')
// const three=document.getElementById('third')
// const four=document.getElementById('fourth')
// const five=document.getElementById('fifth')

// const form = document.querySelector('.rate-form')
// const confirmBox = document.getElementById('confirm-box')
// const csrf = document.getElementsByName('csrfmiddlewaretoken')
// console.log(form)
// console.log(confirmBox)
// console.log(csrf)
// const handleStartSelect=(size)=>{
//     const children = form.children
//     for (let i=0 ; i<children.length;i++){
//         if(i<=size){
//             children[i].classList.add('checked')
//         }else{
//             children[i].classList.remove('checked')
//         }
//     }
//     console.log(children[4])
// }


// const handleSelect=(selection)=>{
//     switch(selection){
//         case 'first':{
//             handleStartSelect(2)
//             return
//         }
//         case 'second':{
//             handleStartSelect(3)
//             return
//         }
//         case 'third':{
//             handleStartSelect(4)
//             return
//         }
//         case 'fourth':{
//             handleStartSelect(5)
//             return
//         }
//         case 'fifth':{
//             handleStartSelect(6)
//             return
//         }
//     }
// }

// const getNumericValue = (stringValue)=>{
//     let numericValue;
//     if(stringValue==='first'){
//         numericValue=1
//     }
//     else if(stringValue==='second'){
//         numericValue=2
//     }
//     else if(stringValue==='third'){
//         numericValue=3
//     }
//     else if(stringValue==='fourth'){
//         numericValue=4
//     }
//     else if(stringValue==='fifth'){
//         numericValue=5
//     }
//     else{
//         numericValue=0
//     }
//     return numericValue
    
// }

// if (one){
//     const arr=[one,two,three,four,five]

// arr.forEach(item=> item.addEventListener('mouseover',(event)=>{
//     handleSelect(event.target.id)
// }))
// arr.forEach(item=> item.addEventListener('click',(event)=>{
//     const val = event.target.id
//     // alert(val)

//     form.addEventListener('submit',e=>{
//         e.preventDefault()
//         const id=e.target.id
//         console.log(id)
//         const val_num=getNumericValue(val)

//         $.ajax({
//             type: 'POST',
//             url :'/shop/review_product/',
//             data:{
//                 'csrfmiddlewaretoken':csrf[0].ariaValueMax,
//                 'el_id':id,
//                 'val':val_num,

//             },
//             success: function(response){
//                 console.log(response)
//                 confirmBox.innerHTML =`<h1>succesfully rated with${response.score}</h1>`

//             },
//             error: function(error){
//                 console.log(error)
//                 confirmBox.innerHTML='<h1>something went wrong</h1>'
//             }

//         })
//     })
// }))
// }