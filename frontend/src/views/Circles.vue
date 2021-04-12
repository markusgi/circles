<template>
    <v-card>

        <p>Circles</p>
    </v-card>
    
</template>

<script>
export default {

  name: "Circles",
  data() {
    return {
      circles: []
    };
  },
  mounted() {
    this.circles = this.getCircles()
  },
  methods: {
    async getCircles() {
      const token = localStorage.getItem("token")
      const res = await fetch(
        "http://localhost:8000/backend/api/circles/list/",
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${ token }`
          },
        }
      );
      const data = await res.json();
      this.circles = data
      console.log(data)
    }
    
}}
</script>
