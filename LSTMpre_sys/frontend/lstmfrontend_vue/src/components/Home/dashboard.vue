<template>
    <el-main class="main-container">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <!-- 核心内容区域 -->
          <component 
            :is="Component" 
            class="content-wrapper"
            :key="$route.path" 
          />
        </transition>
      </router-view>
    </el-main>
  </template>
  
  <script>
  export default {
    name: 'DashboardMain'
  }
  </script>
  
  <style scoped>
  /* 核心布局样式 */
  .el-main.main-container {
    height: calc(100vh - 60px); /* 60px=顶部导航高度 */
    padding: 0 !important; /* 清除默认内边距 */
    overflow: hidden; /* 禁用外部滚动 */
  }
  
  .content-wrapper {
    height: 100%;
    overflow-y: auto; /* 内部滚动 */
    padding: 20px;
    background: #f5f7fa;
  }
  
  /* 过渡动画 */
  .fade-enter-active {
    transition: opacity 0.3s ease-out;
  }
  .fade-leave-active {
    transition: opacity 0.2s ease-in;
  }
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>