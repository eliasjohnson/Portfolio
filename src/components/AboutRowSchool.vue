<template>
  <div class="about-wrapper">
    <div class="about-me">
      <h2 class="about-header">BS Information Systems & Computer Science Minor</h2>
      <ul>
        <li>
          Object Oriented Programming - Python
        </li>
        <li>
          Data Structures and Algorithms - Python
        </li>
        <li>
          Database Theory - MySQL
        </li>
        <li>
          Data Science - Python & R
        </li>
        <li>
          Web Application Development - Full Stack
        </li>
        <li>
          Advanced Statistical Methods - R
        </li>
        <li>
          Data Security Analytics - Kali Linux
        </li>
        <li>
          Marketing & Organizational Behavior
        </li>
        <li>
          Business Intelligence - Tableau
        </li>
      </ul>
    </div>
    <div class="image animate__animated animate__zoomInDown animate__delay-2s">
      <img class="logo" src="../assets/UVU.svg" alt="UVU Logo" height="150px" width="150px"/>
    </div>
  </div>
</template>

<script>
import 'animate.css'

export default {
  name: "AboutRow"
}

</script>

<style scoped>


.image{
  display: block;
}

.about-wrapper {
  color: white;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  background: linear-gradient(110deg, #282828 85%, #fa7c30 85%);
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  border-radius: 20px;
  margin-top: 20px;
  box-shadow: 0px 0px 80px 20px black;
}

.about-header{
  font-size: 28px;
  padding: 10px;
  border-bottom: 2px solid #fa7c30;
}

.about-me{
  padding-left: 50px;
  padding-right: 100px;
  width: 60%;
  text-align: left;
  line-height: 2;
  font-weight: 500;
  font-size: 20px;
}

.image{
  padding: 20px;
  background-color: white;
  margin-top: auto;
  margin-bottom: auto;
  border-radius: 10px;
}


.skills-wrapper{
  display: flex;
  margin-bottom: 25px;
  margin-top: 50px;
  margin-right: 50px;
  width: 30%;
  height: 300px;
  flex-direction: column  ;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  border-radius: 25px;
  background-color: #FFFFFF;
}

.skill-row{
  display: flex;
  height: 100px;
  flex-direction: row;
  justify-content: space-around;
  margin-top: 30px;
  margin-bottom: 30px;
}


@media only screen and (max-width: 1090px){

  li{
    font-size: 14px;
  }

  .image{
    width: 30%;
    margin-left: auto;
    margin-right: auto;
  }

  .about-wrapper{
    flex-direction: column;
  }

  .about-header{
    font-size: 20px;
  }

  .about-me{
    display: flex;
    flex-direction: column;
    padding: 0;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  }

  .skills-wrapper{
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    border-radius: 25px;
  }

  .logo{
    width: 50px;
    height: 50px;
  }

}
</style>
