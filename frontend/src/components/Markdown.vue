<template>
    <markdown-it-vue class="md-body" :content="source"/>
</template>

<script>
    import MarkdownItVue from 'markdown-it-vue'
    import 'markdown-it-vue/dist/markdown-it-vue.css'

    export default {
        props: {
            source: String
        },
        components: {
            MarkdownItVue
        }
    }
</script>

<style scoped>

</style>