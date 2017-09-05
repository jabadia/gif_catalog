<template>
    <div>
        <div class="row mb-4">
            <div class="col">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="search" v-model="q" autofocus>
                    <span class="input-group-addon" @click="q=''">&times;</span>
                </div>
                <div class="dropdown" :class="{show: suggestions.length}">
                    <div class="dropdown-menu" :class="{show: suggestions.length}">
                        <a class="dropdown-item"
                           v-for="suggestion in suggestions"
                           @click="selectSuggestion(suggestion)">{{suggestion}}</a>
                    </div>
                </div>
            </div>
            <div class="col">
                <button @click="reloadPics" class="btn btn-primary">show others...</button>
            </div>
        </div>
        <div class="row">
            <gif-pic v-for="pic in pics" :key="pic.id" :pic="pic"></gif-pic>
        </div>
    </div>
</template>

<script>
    import gifPicsApi from '../services/gifPicsApi.js';
    import GifPic from './GifPic.vue';

    export default {
        data() {
            return {
                pics: [],
                q: '',
                suggestions: [],
                dontGetSuggestions: false,
            };
        },
        watch: {
            q() {
                if (this.q) {
                    this.getSuggestions(this.q);
                    this.searchFor(this.q);
                }
                else {
                    this.reloadPics();
                    this.suggestions = [];
                }
            },
        },
        methods: {
            reloadPics() {
                gifPicsApi.getRandomPics().then(pics => {
                    this.pics = pics;
                });
            },
            searchFor(q) {
                gifPicsApi.search(q).then(pics => {
                    this.pics = pics;
                });
            },
            getSuggestions(q) {
                if (this.dontGetSuggestions) {
                    this.dontGetSuggestions = false;
                    return;
                }
                gifPicsApi.getSuggestions(q).then(suggestions => {
                    this.suggestions = suggestions.slice(0, 8);
                })
            },
            selectSuggestion(suggestion) {
                this.dontGetSuggestions = true;
                this.q = suggestion;
                this.$nextTick(() => {
                    this.suggestions = [];
                });
            },
        },
        created() {
            this.reloadPics();
        },
        components: {
            GifPic,
        },
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
