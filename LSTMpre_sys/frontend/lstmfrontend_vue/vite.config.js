import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'


// https://vite.dev/config/
export default defineConfig({
  server:{
    open:true,  //自动打开浏览器
    port: 9013 //端口
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    }
  },
  plugins: [
    vue(),
    //elementplus自动导入插件
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
})
