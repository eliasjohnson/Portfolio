function onPageLoad() {
    //This will wire up all the event handlers
    document.getElementById('createBtn').onclick = onCreateBtnClicked;
    document.getElementById('cancelBtn').onclick = onCancelBtnClicked;
    document.getElementById('newBtn').onclick = onNewBtnClicked;
  
    //This will Populate the table
    var items = modelGetAllStudents();
    for (var i = 0; i < items.length; i++) {
      addTableItem(items[i]);
    }

    //Resets the input form
    clearInputForm();
  }
  
  function onNewBtnClicked() {
    document.getElementById('formTitle').innerText = 'Create New Student';
  
    document.getElementById('studentEditArea').style.display = 'block';
    document.getElementById('studentListArea').style.display = 'none';
    document.getElementById('createBtn').style.display = 'inline';
    document.getElementById('updateBtn').style.display = 'none';
  }
  
  function onCancelBtnClicked() {
    clearInputForm();
  }
  
  function onEditBtnClicked(id) {
    // Fetch our student record from the store.
    var student = modelGetAllStudent(id);
    if (!student) {
      alert('Unable to find student ID = ' + id);
    }
  
    // Set the form's title
    document.getElementById('formTitle').innerText = 'Edit Student';
  
    // Populate all the form controls.
    var form = document.forms['editForm'];
    form.firstNameEdit.value = student.firstName;
    form.lastNameEdit.value = student.lastName;
  
    if (student.male) {
      form.gender[0].checked = true;
    } else {
      form.gender[1].checked = true;
    }
  
    form.uvuIdEdit.value = student.uvuId;
  
    for (var race in form.raceSelect.options) {
      var option = form.raceSelect.options[race];
      if (option.value === student.race) {
        option.selected = true;
      }
    }
  
    form.ageEdit.value = student.age;
  
    form.isVeteran.checked = student.isVeteran;
  
    // Show the form, hide the contact list.
    document.getElementById('studentEditArea').style.display = 'block';
    document.getElementById('studentListArea').style.display = 'none';
    document.getElementById('createBtn').style.display = 'none';
  
    var updateBtn = document.getElementById('updateBtn');
    updateBtn.style.display = 'inline';
    updateBtn.onclick = function () {
      onUpdateBtnClicked(student.id);
    };
  }
  
  function onUpdateBtnClicked(id) {
    if (!validateControls()) {
      return;
    }
  
    var form = document.forms['editForm'];
    var student = modelUpdateStudent(
      id,
      form.firstNameEdit.value,
      form.lastNameEdit.value,
      form.genderMaleRadio.checked,
      parseInt(form.uvuIdEdit.value),
      form.raceSelect.value,
      parseInt(form.ageEdit.value),
      form.isVeteran.checked
    );
  
    if (!student) {
      alert('Unable to update student ID=' + id);
      return;
    }
  
    // Update the row in the table
    var tr = document.getElementById('row' + id);
    tr.childNodes[0].innerText = student.uvuId;
    tr.childNodes[1].innerText = student.sortableName();
    tr.childNodes[2].innerText = student.male ? 'Male' : 'Female';
  
    // Reset the form and show the list
    clearInputForm();
  }
  
  function onCreateBtnClicked() {
    if (!validateControls()) {
      return;
    }
  
    var form = document.forms['editForm'];
    var newStudent = modelCreateStudent(
      form.firstNameEdit.value,
      form.lastNameEdit.value,
      form.genderMaleRadio.checked,
      parseInt(form.uvuIdEdit.value),
      form.raceSelect.value,
      parseInt(form.ageEdit.value),
      form.isVeteran.checked
    );
  
    addTableItem(newStudent);
  
    clearInputForm();
  }
  
  function addTableItem(student) {
    var table = document.getElementById('studentTable');
  
    var row = table.insertRow(table.rows.length);
    row.id = 'row' + student.id;
  
    var cell = row.insertCell(0);
    cell.innerText = student.uvuId;
  
    var cell = row.insertCell(1);
    cell.innerText = student.sortableName();
  
    var cell = row.insertCell(2);
    cell.innerText = student.male ? 'Male' : 'Female';
  
    var editBtn = document.createElement('button');
    editBtn.type = 'button';
    editBtn.setAttribute('id', 'editBtn');
    editBtn.innerText = 'Edit';
    editBtn.onclick = function () {
      onEditBtnClicked(student.id);
    };
  
    cell = row.insertCell(3);
    cell.appendChild(editBtn);
  
    var deleteBtn = document.createElement('button');
    deleteBtn.type = 'button';
    deleteBtn.setAttribute('id', 'deleteBtn');
    deleteBtn.innerText = 'Delete';
    deleteBtn.onclick = function () {
      onDeleteBtnClicked(student.id);
    };
  
    cell = row.insertCell(4);
    cell.appendChild(deleteBtn);
  }
  
  function validateControls() {
    var form = document.forms['editForm'];
    var isValidated = true;
  
    if (form.firstNameEdit.value === '') {
      document.getElementById('firstNameError').innerText =
        'First name is required.';
      isValidated = false;
    } else {
      document.getElementById('firstNameError').innerText = '';
    }
  
    if (form.lastNameEdit.value === '') {
      document.getElementById('lastNameError').innerText =
        'Last name is required.';
      isValidated = false;
    } else {
      document.getElementById('lastNameError').innerText = '';
    }
  
    if (!form.genderMaleRadio.checked && !form.genderFemaleRadio.checked) {
      document.getElementById('genderError').innerText = 'Gender not given.';
      isValidated = false;
    } else {
      document.getElementById('genderError').innerText = '';
    }
  
    if (form.uvuIdEdit.value === '') {
      document.getElementById('uvuIdError').innerText = 'UVU ID is required.';
      isValidated = false;
    } else if (form.uvuIdEdit.value.length !== 8) {
      document.getElementById('uvuIdError').innerText =
        'UVU ID must be eight digits.';
      isValidated = false;
    } else if (isNaN(parseInt(form.uvuIdEdit.value))) {
      document.getElementById('uvuIdError').innerText =
        'UVU ID  must be a number.';
      isValidated = false;
    } else {
      document.getElementById('uvuIdError').innerText = '';
    }
  
    if (form.raceSelect.selectedIndex === -1) {
      document.getElementById('raceError').innerText = 'Race is is required.';
      isValidated = false;
    } else {
      document.getElementById('raceError').innerText = '';
    }
  
    if (form.ageEdit.value === '') {
      document.getElementById('ageError').innerText = 'Age is required.';
      isValidated = false;
    } else if (isNaN(parseInt(form.ageEdit.value))) {
      document.getElementById('ageError').innerText = 'Age must be a number.';
      isValidated = false;
    } else if (
      parseInt(form.ageEdit.value) < 1 ||
      parseInt(form.ageEdit.value) > 110
    ) {
      document.getElementById('ageError').innerText =
        'Age must be between 1 and 110.';
    } else {
      document.getElementById('ageError').innerText = '';
    }
  
    return isValidated;
  }
  
  function clearInputForm() {
    // Hide the form, show the contact list.
    document.getElementById('studentEditArea').style.display = 'none';
    document.getElementById('studentListArea').style.display = 'block';
  
    // Clear out all the controls on the form.
    var form = document.forms['editForm'];
  
    form.firstNameEdit.value = '';
    document.getElementById('firstNameError').innerText = '';
  
    form.lastNameEdit.value = '';
    document.getElementById('lastNameError').innerText = '';
  
    form.genderMaleRadio.checked = false;
    form.genderFemaleRadio.checked = false;
    document.getElementById('genderError').innerText = '';
  
    form.uvuIdEdit.value = '';
    document.getElementById('uvuIdError').innerText = '';
  
    form.raceSelect.selectedIndex = -1;
    document.getElementById('raceError').innerText = '';
  
    form.ageEdit.value = '';
    document.getElementById('ageError').innerText = '';
  
    form.isVeteran.checked = false;
  }
  
  function onDeleteBtnClicked(id) {
    var student = modelGetAllStudent(id);
    if (!student) {
      alert('Unable to find student ID=' + id);
      return;
    }
  
    if (
      !confirm(
        'Are you sure you want to delete ' +
          student.firstName +
          ' ' +
          student.lastName +
          '?'
      )
    ) {
      return;
    }
  
    modelDeleteStudent(id);
  
    var tr = document.getElementById('row' + id);
    tr.remove();
  }
  