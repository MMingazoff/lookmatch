<template>
  <nav>
    <div class="logo">LOOKMATCH</div>
    <div class="nav-buttons">
      <button>Text Button 1</button>
      <button>Text Button 2</button>
    </div>
    <div class="nav-buttons">
      <button>Text Button 3</button>
      <button>Text Button 4</button>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #333;
  color: #fff;
}

button {
  padding: 10px 20px;
  font-size: 1em;
}

.logo {
  font-size: 1.5em;
}

.nav-buttons {
  display: flex;
  gap: 15px;
}

</style>