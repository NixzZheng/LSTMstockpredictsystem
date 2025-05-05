<template>
       <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <asidelist @menu-select="handleMenuSelect" />
      </el-aside>
      <el-container>
        <el-header>
          <headermenu />
        </el-header>
        </el-container>
        <el-container>
        <el-main>
          <dashboard />
        </el-main>
        </el-container>
    </el-container>
  </div>


</template>

<script setup>
import { ref } from "vue"
import { useRoute } from "vue-router";
import asidelist from "../components/Home/asidelist.vue";
import dashboard from "../components/Home/dashboard.vue";
import headermenu from "../components/Home/headermenu.vue";

const route = useRoute();
const activeIndex = ref(route.path);

</script>

<style scoped>
</style>