<script setup>
import Desktop from "@/components/desktop.vue";
import Header from "@/components/header.vue";
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<template>
  <div v-if="route.name !== 'Login'">
    <Header/>
    <div class="page-container">
      <Desktop/>
      <!-- MAIN CONTENT-->
      <router-view></router-view>
      <!-- END MAIN CONTENT-->
      <!-- END PAGE CONTAINER-->
    </div>
  </div>
  <div v-else>
    <!-- MAIN CONTENT-->
    <router-view></router-view>
    <!-- END MAIN CONTENT-->
  </div>
</template>

<style scoped>

</style>
