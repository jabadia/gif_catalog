<template>
    <div class="row">
        <div class="col-12">
            <ul>
            <li v-for="pic in pics">{{pic.id}}.- {{pic.title}}</li>
            </ul>
        </div>
    </div>
</template>

<script>
    import gifPicsApi from '../services/gifPicsApi.js';

    export default {
        data() {
            return {
                pics: [],
            };
        },
        mounted() {
            gifPicsApi.getRandomPics().then(pics => {
                this.pics = pics;
            });
        }
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
