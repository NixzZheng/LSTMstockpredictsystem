<script>
import {ref} from 'vue'
import { Edit, View as IconView } from '@element-plus/icons-vue'
// let Else = ref([
//     {id:1,title:'注册',icon:UserFilled},
//     {id:2,title:'帮助',icon:ArrowDown},
//     {id:3,title:'登录',icon:Search},
// ])



  </script>


<template>
    <div>
    <div class="header">
        <!-- <div class="header-search">
            <el-input
                v-model="input3"
                placeholder="请输入内容"
                class="input-with-select"
                >
            <template #prepend>
                <el-button :icon="Search" />
            </template>
            </el-input>
        </div> -->
        <div class="header-right">
            <!-- <el-link :icon="UserFilled">登录</el-link> -->
              <!-- 登录链接 -->
        <router-link to="/login" custom v-slot="{ navigate }">
        <el-link 
         :icon="UserFilled" 
          @click="navigate" 
         class="nav-link"
         > 登录
        </el-link>
        </router-link>
            <el-link  target="_blank">注册</el-link>
            <el-link :icon="Edit">帮助</el-link> 
            
            <!-- <el-dropdown>
                <span class="el-dropdown-link">
                其他
                <el-icon class="el-icon--right">
                    <arrow-down />
                </el-icon>
                </span>
            </el-dropdown> -->
        </div>
    </div>
    </div>

  </template>
  

  

  <style scoped>
  /* 页面头部 */
.el-header {
    min-width: 1200px;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
    flex: 1;
    position:fixed;
    top:0;
    left: 200px;
    width: calc(100vw - 200px);
    background-color: #f9def0;
    z-index: 999;
    padding: 0 0;
}

.header-search {
    display: flex;
    flex: 1;
    margin: 0 20px;
}
/* 按钮的颜色  */
.header .el-input-group__append {
    background-color: var(--el-color-primary);
    color: #fff;
}

.header-right {
  display: flex;
  justify-content: flex-end; /* 内容靠右对齐 */
  gap: 20px; /* 元素之间的间距 */
}

.header-right .el-link {
    flex: 1;
    margin: 0 20px;
}
/* focus伪类选择器：可以用来选取获得焦点的元素
当鼠标移入上去后取消黑色边框 */
.el-dropdown-link:focus{
   outline: none;
}
  </style>