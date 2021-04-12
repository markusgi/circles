<template>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      src="../assets/avatar.png"
    ></v-img>

    <v-card-title>{{person.vorname}} {{person.nachname}}, {{person.anstellungsart}}</v-card-title>

    <v-card-text>

      <div class="my-4 subtitle-1">
        Team: {{person.team}}, {{person.standort}}
      </div>

      <div>Vorgesetzter: {{ person.vorgesetzter }}</div>
    </v-card-text>

    <v-card-title>{{person.position}}</v-card-title>

  </v-card>
</template>

<script>
export default {
    data: () => ({
      loading: false,
      selection: 1,
    }),

    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
    },

    props: {
        person: Object
    }
}
</script>