var studentList = [];

var nextStudentId = 1000;

function Student(firstName, lastName, male, uvuId, race, age, isVeteran) {
  this.id = nextStudentId++;
  this.firstName = firstName;
  this.lastName = lastName;
  this.male = male;
  this.uvuId = uvuId;
  this.race = race;
  this.age = age;
  this.isVeteran = isVeteran;

  this.sortableName = function () {
    return this.lastName + ', ' + this.firstName;
  };
}

function modelCreateStudent(
  firstName,
  lastName,
  male,
  uvuId,
  race,
  age,
  isVeteran
) {
  var newStudent = new Student(
    firstName,
    lastName,
    male,
    uvuId,
    race,
    age,
    isVeteran
  );
  studentList.push(newStudent);
  return newStudent;
}

function modelGetAllStudents() {
  return studentList;
}

function modelGetAllStudent(id) {
  for (x in studentList) {
    if (studentList[x].id == id) {
      return studentList[x];
    }
  }

  return undefined;
}
function modelUpdateStudent(
  id,
  firstName,
  lastName,
  male,
  uvuId,
  race,
  age,
  isVeteran
) {
  var student = modelGetAllStudent(id);
  if (!student) {
    return undefined;
  }

  student.firstName = firstName;
  student.lastName = lastName;
  student.male = male;
  student.uvuId = uvuId;
  student.race = race;
  student.age = age;
  student.isVeteran = isVeteran;

  return student;
}

function modelDeleteStudent(id) {
  for (var x in studentList) {
    if (studentList[x].id === id) {
      studentList.splice(x, 1);
      break;
    }
  }
}
