// buttons
const bio = document.getElementsByClassName("nav-btns")[0];
const education = document.getElementsByClassName("nav-btns")[1];
const experience = document.getElementsByClassName("nav-btns")[2];

// (El) elements
const bioEl = document.getElementsByClassName("content")[0];
const educationEl = document.getElementsByClassName("content")[1];
const experienceEl = document.getElementsByClassName("content")[2];


bio.addEventListener("click", e => {
    bio.classList.add("active-right");
    education.classList.remove("active-right");
    experience.classList.remove("active-right");
    
    education.firstElementChild.classList.remove("design");
    experience.firstElementChild.classList.remove("design");
    
    bioEl.classList.add("show");
    educationEl.classList.remove("show");
    experienceEl.classList.remove("show");
});

education.addEventListener("click", e => {
    bio.classList.remove("active-right");
    education.classList.add("active-right");
    experience.classList.remove("active-right");
    
    education.firstElementChild.classList.add("design");
    experience.firstElementChild.classList.remove("design");
    
    bioEl.classList.remove("show");
    educationEl.classList.add("show");
    experienceEl.classList.remove("show");
});


experience.addEventListener("click", e => {
    bio.classList.remove("active-right");
    education.classList.remove("active-right");
    experience.classList.add("active-right");
    
    education.firstElementChild.classList.remove("design");
    experience.firstElementChild.classList.add("design");

    bioEl.classList.remove("show");
    educationEl.classList.remove("show");
    experienceEl.classList.add("show");
});





// Scripts for chat window

// MESSAGE INPUT
const textarea = document.querySelector('.chatbox-message-input')
const chatboxForm = document.querySelector('.chatbox-message-form')

textarea.addEventListener('input', function () {
	let line = textarea.value.split('\n').length

	if(textarea.rows < 6 || line < 6) {
		textarea.rows = line
	}

	if(textarea.rows > 1) {
		chatboxForm.style.alignItems = 'flex-end'
	} else {
		chatboxForm.style.alignItems = 'center'
	}
})
textarea.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    event.preventDefault(); // Prevents the default behavior of the "Enter" key
    writeMessage();
	setTimeout(autoReply, 1000);
  }
});


// TOGGLE CHATBOX
const chatboxToggle = document.querySelector('.chatbox-toggle')
const chatboxMessage = document.querySelector('.chatbox-message-wrapper')

chatboxToggle.addEventListener('click', function () {
	chatboxMessage.classList.toggle('show')
})



// DROPDOWN TOGGLE
const dropdownToggle = document.querySelector('.chatbox-message-dropdown-toggle')
const dropdownMenu = document.querySelector('.chatbox-message-dropdown-menu')

dropdownToggle.addEventListener('click', function () {
	dropdownMenu.classList.toggle('show')
})

document.addEventListener('click', function (e) {
	if(!e.target.matches('.chatbox-message-dropdown, .chatbox-message-dropdown *')) {
		dropdownMenu.classList.remove('show')
	}
})



// CHATBOX MESSAGE
const chatboxMessageWrapper = document.querySelector('.chatbox-message-content')
const chatboxNoMessage = document.querySelector('.chatbox-message-no-message')

chatboxForm.addEventListener('submit', function (e) {
	e.preventDefault()

	if(isValid(textarea.value)) {
		writeMessage()
		setTimeout(autoReply, 500)
	}
})



function addZero(num) {
	return num < 10 ? '0'+num : num
}

function writeMessage() {
	const today = new Date()
	let message = `
		<div class="chatbox-message-item sent">
			<span class="chatbox-message-item-text">
				${textarea.value.trim().replace(/\n/g, '<br>\n')}
			</span>
			<span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
		</div>
	`
	chatboxMessageWrapper.insertAdjacentHTML('beforeend', message)
	chatboxForm.style.alignItems = 'center'
	textarea.rows = 1
	textarea.focus()
	textarea.value = ''
	chatboxNoMessage.style.display = 'none'
	scrollBottom()
}

function autoReply() {
	const today = new Date()
	let message = `
		<div class="chatbox-message-item received">
			<span class="chatbox-message-item-text">
				Hi there! These are just some demo messages since the site is still under development. Thank you for tuning in!
			</span>
			<span class="chatbox-message-item-time">${addZero(today.getHours())}:${addZero(today.getMinutes())}</span>
		</div>
	`
	chatboxMessageWrapper.insertAdjacentHTML('beforeend', message)
	scrollBottom()
}

function scrollBottom() {
	chatboxMessageWrapper.scrollTo(0, chatboxMessageWrapper.scrollHeight)
}

function isValid(value) {
	let text = value.replace(/\n/g, '')
	text = text.replace(/\s/g, '')

	return text.length > 0
}

$(".chatbox-message-input").keypress(function (e) {
    if (e.which == 13) {
        autoReply();
    }
});