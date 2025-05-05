<script setup>  
import {ref} from 'vue'
import { useRoute } from 'vue-router'
//const isCollapse = ref(true)
import {
  Document,
  Menu as IconMenu,
  Operation,
  Filter,
  TrendCharts,
  DataAnalysis,
} from '@element-plus/icons-vue'
let asidelist = ref([
    {id:1,title:'今日行情',icon:TrendCharts,path:'/dashboard/search'},
    {id:2,title:'智能选股',icon:Filter},
    {id:3,title:'模型调试',icon:Operation},
    {id:4,title:'一键预测',icon:DataAnalysis},
])
const route = useRoute()

// 菜单配置添加路由路径
// let asidelist = ref([
//   { id:1, title:'今日行情', icon:TrendCharts, path:'/dashboard/search' },
//   { id:2, title:'智能选股', icon:Filter, path:'/dashboard/analysis' },
//   { id:3, title:'模型调试', icon:Operation, path:'/dashboard/test' },
//   { id:4, title:'一键预测', icon:DataAnalysis, path:'/dashboard/predict' }
// ])

// 动态设置激活菜单
const activeIndex = computed(() => {
  return asidelist.value.find(item => item.path === route.path)?.path
})

</script>  

<template>
    <el-aside width="200px" class="aside">
    <div class="aside-list">
    <h5 class="mb-2" style="background-color: #f689d2; 
     width: 200px; height: 70px;
     display: inline-block; text-align: center; 
     line-height: 70px;font-size: 20px;margin: 0; padding: 0;"
     >Stock-Analysis</h5>
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            :collapse="isCollapse"
            @open="handleOpen"
            @close="handleClose"
        >
        
        <el-menu-item index="v.id" v-for="v in asidelist":key="v.id">
        <el-icon><component :is= "v.icon" ></component></el-icon>
        <template #title>{{v.title}}</template>
        </el-menu-item>
        </el-menu>
</div>
</el-aside>
</template>

<style scoped>
/* 左侧导航栏 */
.aside {
    
    width: 200px;
    position:auto;
}
.aside-list {
    top: 0;
    position: fixed;
    left: 0;
    width: 200px;
    

}

.aside .el-radio-group{
    height: 70px;
    font-size: 36px;
    font-weight: 500;
    background-color: #f689d2;
}

.aside .el-menu {
    height:100vh;
    
    
}
/* 字体图标的样式 */
.aside i {
    font-size: 24px;
    font-weight: 500;
    margin-right: 5px;
}
.aside .el-radio-button__inner {
    border:none;
    font-size: 20px;
}



</style>