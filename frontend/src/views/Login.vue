<template>
    <v-app>
        <v-card width="400" class="mx-auto mt-5 pa-4">
            <v-card-title class="pb-0">
                <v-img
                    alt="planted logo"
                    class="shrink mt-1 hidden-sm-and-down"
                    contain
                    min-width="100"
                    :src="require('@/assets/planted.svg')"
                    width="100"
                />
            </v-card-title>
            <v-card-text>
                <v-form @submit.prevent="login">
                    <v-text-field
                        v-model="username"
                        label="Username"
                        prepend-icon="mdi-account-circle"
                    />
                    <v-text-field
                        v-model="password"
                        :type="showPassword ? 'text' : 'password'"
                        label="Password"
                        prepend-icon="mdi-lock"
                        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="showPassword = !showPassword"
                    />
                    <v-card-actions>
                        <v-btn :loading="loading" type="submit" color="primary"
                            >Login</v-btn
                        >
                    </v-card-actions>
                </v-form>
            </v-card-text>
        </v-card>
    </v-app>
</template>

<script>

export default {

  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      showPassword: false,
      loading: false
    };
  },
  methods: {
    async login() {
      const { username, password } = this;
      const res = await fetch(
        "http://localhost:8000/backend/api/auth/token/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ username, password })
        }
      );
      const data = await res.json();
      localStorage.setItem("token", data.access);
      this.$router.push({ path: "/" })
    }
  }
};
</script>
