<template>
  <div class="home">
      <v-list-item dense v-for="person in persons" :key="person.vorname" class="pl-0">
        <Profile 
          :person="person" 
        />
    </v-list-item>
  </div>
</template>

<script>
import Profile from '@/components/Profile.vue'

export default {

  name: "Home",
  data() {
    return {
      persons: []
    };
  },
  mounted() {
    this.persons = this.getPersons()
  },
  methods: {
    async getPersons() {
      const token = localStorage.getItem("token")
      const res = await fetch(
        "http://localhost:8000/backend/api/persons/list/",
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${ token }`
          },
        }
      );
      const data = await res.json();
      this.persons = data
    }
  },
  components: {
    Profile
  }
};
</script>
