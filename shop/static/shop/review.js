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
    for (let i=0; i < children.length; i++) {
        if(i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
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
            // jQuery.noConflict();
            jQuery_3_6_3.ajax({
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
                    confirmBox.innerHTML = `<h4>Successfully rated with ${response.score}</h4>`
                },
                error: function(error){
                    // console.log(error)
                    confirmBox.innerHTML = '<h4>Ups... something went wrong</h4>'
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
// jQuery_3_6_3('#submit_review').click(function (event){
// jQuery_3_6_3("#review_form").submit(function (e){
    // e.preventDefault();
jQuery_3_6_3(document).on('submit','#review-form', function(e){
    e.preventDefault()
    // jQuery.noConflict();
    jQuery_3_6_3.ajax({
    url : "/shop/review_product/",
    type : "POST", // http method
    data : {
        prodID:jQuery_3_6_3('#prodID').val(),
        review:jQuery_3_6_3('#review').val(),
      csrfmiddlewaretoken: jQuery_3_6_3('input[name=csrfmiddlewaretoken]').val() , //This is must for security in Django
    }, // data sent with the post request

    // handle a successful response
    success: function(response){
        // console.log(response)
        confirmBox.innerHTML = `<h4>Successfully reviewed , If you haven't rated the product yet ,Please click on the stars to rate it </h4>`
        return
    },
    error: function(error){
        // console.log(error)
        confirmBox.innerHTML = '<h4>Ups... something went wrong</h1>'
        return
    }
})

});

