console.log("JavaScript loaded!");

const radios = document.querySelectorAll('input[name="send_type"]');
const singleEmail = document.getElementById('single-email-section');
const groupEmail = document.getElementById('group-email-section');

function updateVisibility() {
  const selected = document.querySelector('input[name="send_type"]:checked').value;

  if (selected === 'single') {
    singleEmail.classList.remove('hidden');
    groupEmail.classList.add('hidden');
    console.log(selected);
  } else {
    singleEmail.classList.add('hidden');
    groupEmail.classList.remove('hidden');
    console.log(selected);

  }
}

// Run on page load
updateVisibility();

// Run on change
radios.forEach(radio => {
  radio.addEventListener('change', updateVisibility);
});

document.addEventListener("DOMContentLoaded" , () => {
  const groupSelect = document.getElementById("group-email");
  const outputDiv = document.getElementById("group-email-show-id");

  // If either element does not exist, stop running this
  if (!groupSelect || !outputDiv) return; 
  groupSelect.addEventListener("change", () => {
    const selectedGroup = groupSelect.value;
    outputDiv.innerHTML = "";

    // If no group is selected or selected group DNE, stop running
    if(!selectedGroup || !GROUPS[selectedGroup]) {
      return;
    }

    const emails = GROUPS[selectedGroup];

    const title = document.createElement("p");
    title.textContent = "Emails in this group:";
    outputDiv.appendChild(title);

    const ul = document.createElement("ul");

    emails.forEach(email => {
      const li = document.createElement("li");
      li.textContent = email;
      ul.appendChild(li);
    });

    outputDiv.appendChild(ul);
  });
});




