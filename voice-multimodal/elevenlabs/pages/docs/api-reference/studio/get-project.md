---
title: "Get Studio Project"
source: https://elevenlabs.io/docs/api-reference/studio/get-project.md
path: docs/api-reference/studio/get-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Studio Project

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}

Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-project

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

### Query parameters

- `share_id` (string, optional, nullable) — The share ID of the project

## Response

### 200

Successful Response

- `project_id` (string, required) — The ID of the project.
- `name` (string, required) — The name of the project.
- `create_date_unix` (integer, required) — The creation date of the project.
- `created_by_user_id` (string, required, nullable) — The user ID who created the project.
- `default_title_voice_ref_id` (string, required) — The default title project voice reference ID.
- `default_paragraph_voice_ref_id` (string, required) — The default paragraph project voice reference ID.
- `default_model_id` (string, required) — The default model ID.
- `can_be_downloaded` (boolean, required) — Whether the project can be downloaded.
- `volume_normalization` (boolean, required) — Whether the project uses volume normalization.
- `state` (enum, required) — The state of the project.
  - Allowed values: `creating`, `default`, `converting`, `in_queue`
- `access_level` (enum, required) — The access level of the project.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `quality_preset` (enum, required, default: standard) — The quality preset level of the project.
  - Allowed values: `standard`, `high`, `ultra`, `ultra_lossless`
- `chapters` (list of object, required) — List of chapters of the project and their metadata.
  - `chapter_id` (string, required) — The ID of the chapter.
  - `name` (string, required) — The name of the chapter.
  - `can_be_downloaded` (boolean, required) — Whether the chapter can be downloaded.
  - `state` (enum, required) — The state of the chapter.
    - Allowed values: `default`, `converting`
  - `last_conversion_date_unix` (integer, optional, nullable) — The last conversion date of the chapter.
  - `conversion_progress` (double, optional, nullable) — The conversion progress of the chapter.
  - `has_video` (boolean, optional, nullable) — Whether the chapter has a video.
  - `has_visual_content` (boolean, optional, nullable) — Whether the chapter has any visual content (video, image, or text clips).
  - `voice_ids` (list of string, optional, nullable) — List of voice ids used by the chapter
  - `statistics` (object, optional, nullable) — The statistics of the chapter.
    - `characters_unconverted` (integer, required) — The number of unconverted characters.
    - `characters_converted` (integer, required) — The number of converted characters.
    - `paragraphs_converted` (integer, required) — The number of converted paragraphs.
    - `paragraphs_unconverted` (integer, required) — The number of unconverted paragraphs.
    - `credits_needed_to_convert` (integer, optional, nullable) — The number of credits needed to convert the remaining paragraphs.
    - `voice_statistics` (list of object, optional, nullable) — Per-voice breakdown of character counts.
      - `project_voice_ref_id` (string, required) — The project voice reference ID.
      - `characters_unconverted` (integer, required) — The number of unconverted characters for this voice.
      - `characters_converted` (integer, required) — The number of converted characters for this voice.
      - `voice_id` (string, required, deprecated) — The voice ID.
      - `credits_needed_to_convert` (integer, optional, nullable) — The number of credits needed to convert the remaining audio for this voice.
  - `last_conversion_error` (string, optional, nullable) — The last conversion error of the chapter.
- `pronunciation_dictionary_versions` (list of object, required) — List of pronunciation dictionary versions of the project and their metadata.
  - `version_id` (string, required)
  - `version_rules_num` (integer, required)
  - `pronunciation_dictionary_id` (string, required)
  - `dictionary_name` (string, required)
  - `version_name` (string, required)
  - `permission_on_resource` (enum, required, nullable)
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `created_by` (string, required)
  - `creation_time_unix` (integer, required)
  - `archived_time_unix` (integer, optional, nullable)
- `pronunciation_dictionary_locators` (list of object, required) — List of pronunciation dictionary locators.
  - `pronunciation_dictionary_id` (string, required)
  - `version_id` (string, required, nullable)
- `apply_text_normalization` (enum, required) — Whether text normalization is applied to the project.
  - Allowed values: `auto`, `on`, `off`, `apply_english`
- `assets` (list of object or object or object, required) — List of uploaded assets e.g. videos, audios.
  - ProjectVideoResponseModel
    - `video_id` (string, required)
    - `filename` (string, required)
    - `signed_url` (string, required, nullable)
    - `signed_preview_url` (string, required, nullable)
    - `offset_ms` (integer, required)
    - `duration_ms` (integer, required)
    - `volume_gain_db` (double, required)
    - `muted` (boolean, required)
    - `width` (integer, required)
    - `height` (integer, required)
    - `codec` (string, required)
    - `order` (string, required)
    - `created_at_ms` (integer, required)
    - `updated_at_ms` (integer, required)
    - `thumbnail_interval_seconds` (double, required)
    - `thumbnail_size` (list of integer, required)
    - `thumbnail_sheets` (list of object, required)
      - `start_thumbnail_index` (integer, required)
      - `thumbnail_count` (integer, required)
      - `signed_cloud_url` (string, required)
    - `start_time_ms` (integer, required)
    - `end_time_ms` (integer, required, nullable)
    - `preview_job_progress` (double, required)
    - `import_speech_progress` (double, required, nullable)
    - `fade_in_ms` (integer, optional, default: 0)
    - `fade_out_ms` (integer, optional, default: 0)
    - `error` (string, optional, nullable)
    - `asset_preview_signed_url` (string, optional, nullable)
    - `source_video_id` (string, optional, nullable)
    - `source_asset_id` (string, optional, nullable)
    - `source_platform_asset_id` (string, optional, nullable)
    - `pending_blocks_metadata` (object, optional, nullable)
      - `target_global_offset_ms` (integer, required, nullable)
      - `block_ids` (list of string, required)
    - `pending_external_audios_metadata` (object, optional, nullable)
      - `target_global_offset_ms` (integer, required, nullable)
      - `external_audio_ids` (list of string, required)
    - `speech_imported` (boolean, optional, default: false)
    - `pending_task` (object, optional, nullable)
      - `type` (enum, required)
        - Allowed values: `preprocessing`, `speech_import`, `dubbing`, `video_to_music`, `media_generation`
      - `progress` (double, optional, default: 0)
      - `started_at_ms` (integer, optional)
      - `updated_at_ms` (integer, optional)
      - `metadata` (map from string to any, optional)
    - `audio_track_ready` (boolean, optional, default: true)
    - `export_format_ready` (boolean, optional, default: true)
    - `current_snapshot_id` (string, optional, nullable)
    - `source_context` (object, optional, nullable)
      - `generation_id` (string, required)
      - `model_id` (string, required)
      - `source_type` ("generation", optional, default: generation)
      - `prompt` (string, optional, nullable)
      - `model_provider` (string, optional, nullable)
      - `generation_session_id` (string, optional, nullable)
      - `session_iteration_id` (string, optional, nullable)
      - `model_parameters` (map from string to any, optional, nullable)
      - `extend_video` (object, optional, nullable)
        - `generation_id` (string, optional, nullable)
        - `content_asset_id` (string, optional, nullable)
        - `template_node_id` (string, optional, nullable)
        - `studio_clip` (object, optional, nullable)
          - `project_id` (string, required)
          - `chapter_id` (string, required)
          - `clip_type` (enum, required)
            - Allowed values: `video`, `image`, `external_audio`, `tts_node`
          - `clip_id` (string, required)
          - `block_id` (string, optional, nullable)
          - `preview_url` (string, optional, nullable)
    - `analysis` (object, optional, nullable)
      - `status` (enum, required)
        - Allowed values: `processing`, `completed`, `failed`
      - `data` (object, required, nullable)
        - `title` (string, required)
        - `description` (string, required)
        - `content_type` (string, optional, nullable)
        - `overall_pacing` (string, optional, nullable)
        - `subjects` (list of object, optional)
          - `name` (string, required)
          - `description` (string, required)
        - `segments` (list of object, optional)
          - `start_ms` (integer, required)
          - `end_ms` (integer, required)
          - `description` (string, required)
          - `subjects` (list of string, optional)
          - `shot_type` (string, optional, nullable)
          - `camera_movement` (string, optional, nullable)
          - `transition_in` (string, optional, nullable)
          - `has_speech` (boolean, optional, default: false)
          - `has_music` (boolean, optional, default: false)
          - `pacing` (string, optional, nullable)
        - `key_moments` (list of object, optional)
          - `timestamp_ms` (integer, required)
          - `type` (string, required)
          - `description` (string, required)
      - `updated_at_ms` (integer, optional)
    - `transcription` (object, optional, nullable)
      - `status` (enum, required)
        - Allowed values: `processing`, `completed`, `failed`
      - `data` (object, required, nullable)
        - `language_code` (string, required)
        - `text` (string, required)
        - `words` (list of string, required)
        - `word_start_times_ms` (list of integer, required)
        - `word_end_times_ms` (list of integer, required)
        - `word_speaker_ids` (list of string, required)
      - `updated_at_ms` (integer, optional)
    - `type` ("video", optional, default: video)
    - `canvas_placement` (object, optional) — Defines asset positioning and transformation on canvas.
      - `x_relative` (double, optional, default: 0.5)
      - `y_relative` (double, optional, default: 0.5)
      - `scale_x` (double, optional, default: 1)
      - `scale_y` (double, optional, default: 1)
      - `pivot_x` (double, optional, default: 0)
      - `pivot_y` (double, optional, default: 0)
      - `skew_x` (double, optional, default: 0)
      - `skew_y` (double, optional, default: 0)
      - `crop_top` (double, optional, default: 0)
      - `crop_right` (double, optional, default: 0)
      - `crop_bottom` (double, optional, default: 0)
      - `crop_left` (double, optional, default: 0)
      - `flip_x` (boolean, optional, default: false)
      - `flip_y` (boolean, optional, default: false)
    - `animation` (object, optional)
      - `enter_effect` (enum, optional, default: none)
        - Allowed values: `none`, `fade`, `float`, `gentle_float`, `zoom_in`, `drop`, `slide_left`, `slide_right`, `slide_up`, `slide_down`, `pop`, `bounce`, `spin`, `slide_bounce`
      - `enter_duration_ms` (integer, optional, default: 0)
      - `exit_effect` (enum, optional, default: none)
        - Allowed values: `none`, `fade`, `float`, `gentle_float`, `zoom_in`, `drop`, `slide_left`, `slide_right`, `slide_up`, `slide_down`, `pop`, `bounce`, `spin`, `slide_bounce`
      - `exit_duration_ms` (integer, optional, default: 0)
    - `playback_speed` (double, optional, default: 1)
    - `opacity` (double, optional, default: 1)
    - `track_id` (string, optional, default: v0)
  - ProjectExternalAudioResponseModel
    - `external_audio_id` (string, required)
    - `filename` (string, required)
    - `signed_url` (string, required, nullable)
    - `offset_ms` (integer, required)
    - `duration_ms` (integer, required)
    - `start_time_ms` (integer, required)
    - `end_time_ms` (integer, required, nullable)
    - `order` (string, required)
    - `track_id` (string, required)
    - `created_at_ms` (integer, required)
    - `updated_at_ms` (integer, required)
    - `import_speech_progress` (double, required, nullable)
    - `volume_gain_db` (double, optional, default: 0)
    - `muted` (boolean, optional, default: false)
    - `fade_in_ms` (integer, optional, default: 0)
    - `fade_out_ms` (integer, optional, default: 0)
    - `source_external_audio_id` (string, optional, nullable)
    - `source_asset_id` (string, optional, nullable)
    - `source_platform_asset_id` (string, optional, nullable)
    - `pending_blocks_metadata` (object, optional, nullable)
      - `target_global_offset_ms` (integer, required, nullable)
      - `block_ids` (list of string, required)
    - `pending_external_audios_metadata` (object, optional, nullable)
      - `target_global_offset_ms` (integer, required, nullable)
      - `external_audio_ids` (list of string, required)
    - `speech_imported` (boolean, optional, default: false)
    - `pending_task` (object, optional, nullable)
      - `type` (enum, required)
        - Allowed values: `preprocessing`, `speech_import`, `dubbing`, `video_to_music`, `media_generation`
      - `progress` (double, optional, default: 0)
      - `started_at_ms` (integer, optional)
      - `updated_at_ms` (integer, optional)
      - `metadata` (map from string to any, optional)
    - `error` (string, optional, nullable)
    - `current_snapshot_id` (string, optional, nullable)
    - `source_context` (object, optional, nullable)
      - `source_type`: `music_explore_song` (MusicExploreSongSourceContext)
        - `music_explore_song_id` (string, required)
        - `bpm` (integer, optional, nullable)
        - `description` (string, optional, nullable)
        - `lyrics` (string, optional, nullable)
        - `title` (string, optional, nullable)
        - `vocals` (string, optional, nullable)
      - `source_type`: `sfx` (SfxSourceContext)
        - `generation_config` (map from string to any, optional, nullable)
        - `sound_generation_history_item_id` (string, optional, nullable)
        - `text` (string, optional, nullable)
      - `source_type`: `song` (SongSourceContext)
        - `song_id` (string, required)
        - `bpm` (integer, optional, nullable)
        - `chat_id` (string, optional, nullable)
        - `description` (string, optional, nullable)
        - `generation_settings` (map from string to any, optional, nullable)
        - `genres` (list of string, optional)
        - `is_explicit` (boolean, optional, nullable)
        - `languages` (list of string, optional)
        - `title` (string, optional, nullable)
    - `analysis` (object, optional, nullable)
      - `status` (enum, required)
        - Allowed values: `processing`, `completed`, `failed`
      - `data` (object, required, nullable)
        - `title` (string, required)
        - `description` (string, required)
        - `content_type` (string, optional, nullable)
        - `overall_pacing` (string, optional, nullable)
        - `segments` (list of object, optional)
          - `start_ms` (integer, required)
          - `end_ms` (integer, required)
          - `description` (string, required)
          - `segment_type` (string, optional, nullable)
          - `has_speech` (boolean, optional, default: false)
          - `has_music` (boolean, optional, default: false)
          - `pacing` (string, optional, nullable)
        - `key_moments` (list of object, optional)
          - `timestamp_ms` (integer, required)
          - `type` (string, required)
          - `description` (string, required)
      - `updated_at_ms` (integer, optional)
    - `transcription` (object, optional, nullable)
      - `status` (enum, required)
        - Allowed values: `processing`, `completed`, `failed`
      - `data` (object, required, nullable)
        - `language_code` (string, required)
        - `text` (string, required)
        - `words` (list of string, required)
        - `word_start_times_ms` (list of integer, required)
        - `word_end_times_ms` (list of integer, required)
        - `word_speaker_ids` (list of string, required)
      - `updated_at_ms` (integer, optional)
    - `type` ("audio", optional, default: audio)
  - ProjectImageResponseModel
    - `image_id` (string, required)
    - `filename` (string, required)
    - `file_size_bytes` (integer, required)
    - `width` (integer, required)
    - `height` (integer, required)
    - `offset_ms` (integer, required)
    - `duration_ms` (integer, required)
    - `order` (string, required)
    - `canvas_placement` (object, required) — Defines asset positioning and transformation on canvas.
      - `x_relative` (double, optional, default: 0.5)
      - `y_relative` (double, optional, default: 0.5)
      - `scale_x` (double, optional, default: 1)
      - `scale_y` (double, optional, default: 1)
      - `pivot_x` (double, optional, default: 0)
      - `pivot_y` (double, optional, default: 0)
      - `skew_x` (double, optional, default: 0)
      - `skew_y` (double, optional, default: 0)
      - `crop_top` (double, optional, default: 0)
      - `crop_right` (double, optional, default: 0)
      - `crop_bottom` (double, optional, default: 0)
      - `crop_left` (double, optional, default: 0)
      - `flip_x` (boolean, optional, default: false)
      - `flip_y` (boolean, optional, default: false)
    - `created_at_ms` (integer, required)
    - `updated_at_ms` (integer, required)
    - `signed_url` (string, optional, nullable)
    - `thumbnail_signed_url` (string, optional, nullable)
    - `type` ("image", optional, default: image)
    - `source` ("upload", optional, default: upload)
    - `track_id` (string, optional, default: v0)
    - `animation` (object, optional)
      - `enter_effect` (enum, optional, default: none)
        - Allowed values: `none`, `fade`, `float`, `gentle_float`, `zoom_in`, `drop`, `slide_left`, `slide_right`, `slide_up`, `slide_down`, `pop`, `bounce`, `spin`, `slide_bounce`
      - `enter_duration_ms` (integer, optional, default: 0)
      - `exit_effect` (enum, optional, default: none)
        - Allowed values: `none`, `fade`, `float`, `gentle_float`, `zoom_in`, `drop`, `slide_left`, `slide_right`, `slide_up`, `slide_down`, `pop`, `bounce`, `spin`, `slide_bounce`
      - `exit_duration_ms` (integer, optional, default: 0)
    - `opacity` (double, optional, default: 1)
    - `current_snapshot_id` (string, optional, nullable)
    - `source_asset_id` (string, optional, nullable)
    - `source_platform_asset_id` (string, optional, nullable)
    - `error` (string, optional, nullable)
    - `pending_task` (object, optional, nullable)
      - `type` (enum, required)
        - Allowed values: `preprocessing`, `speech_import`, `dubbing`, `video_to_music`, `media_generation`
      - `progress` (double, optional, default: 0)
      - `started_at_ms` (integer, optional)
      - `updated_at_ms` (integer, optional)
      - `metadata` (map from string to any, optional)
    - `analysis` (object, optional, nullable)
      - `status` (enum, required)
        - Allowed values: `processing`, `completed`, `failed`
      - `data` (object, required, nullable)
        - `title` (string, required)
        - `description` (string, required)
        - `content_type` (string, optional, nullable)
        - `mood_and_style` (string, optional, nullable)
        - `composition_notes` (string, optional, nullable)
        - `visible_text` (string, optional, nullable) — Readable text overlaid or shown in the image, if any.
        - `subjects` (list of object, optional)
          - `name` (string, required)
          - `description` (string, required)
      - `updated_at_ms` (integer, optional)
- `voices` (list of object, required) — List of configured project voices.
  - `project_voice_ref_id` (string, required)
  - `voice_id` (string, required)
  - `alias` (string, required)
  - `stability` (double, required)
  - `similarity_boost` (double, required)
  - `style` (double, required)
  - `is_pinned` (boolean, required)
  - `use_speaker_boost` (boolean, required)
  - `volume_gain` (double, required)
  - `speed` (double, required)
- `quality_check_on` (boolean, required, deprecated) — Whether quality check is enabled for this project.
- `quality_check_on_when_bulk_convert` (boolean, required, deprecated) — Whether quality check is enabled on the project when bulk converting.
- `default_title_voice_id` (string, required, deprecated) — The default title voice ID.
- `default_paragraph_voice_id` (string, required, deprecated) — The default paragraph voice ID.
- `last_conversion_date_unix` (integer, optional, nullable) — The last conversion date of the project.
- `title` (string, optional, nullable) — The title of the project.
- `author` (string, optional, nullable) — The author of the project.
- `description` (string, optional, nullable) — The description of the project.
- `genres` (list of string, optional, nullable) — List of genres of the project.
- `cover_image_url` (string, optional, nullable) — The cover image URL of the project.
- `target_audience` (enum, optional, nullable) — The target audience of the project.
  - Allowed values: `children`, `young adult`, `adult`, `all ages`
- `language` (string, optional, nullable) — Two-letter language code (ISO 639-1) of the language of the project.
- `content_type` (string, optional, nullable) — The content type of the project, e.g. 'Novel' or 'Short Story'
- `original_publication_date` (string, optional, nullable) — The original publication date of the project.
- `mature_content` (boolean, optional, nullable) — Whether the project contains mature content.
- `isbn_number` (string, optional, nullable) — The ISBN number of the project.
- `fiction` (enum, optional, nullable) — Whether the project is fiction.
  - Allowed values: `fiction`, `non-fiction`
- `creation_meta` (object, optional, nullable) — The creation meta of the project.
  - `creation_progress` (double, required) — The progress of the project creation.
  - `status` (enum, required) — The status of the project creation action.
    - Allowed values: `draft`, `pending`, `creating`, `finished`, `failed`
  - `type` (enum, required) — The type of the project creation action.
    - Allowed values: `blank`, `generate_podcast`, `auto_assign_voices`, `dub_video`, `import_speech`
- `source_type` (enum, optional, nullable) — The source type of the project.
  - Allowed values: `blank`, `book`, `article`, `genfm`, `video`, `screenplay`
- `chapters_enabled` (boolean, optional, nullable, default: true) — Whether chapters are enabled for the project.
- `captions_enabled` (boolean, optional, nullable, default: true) — Whether captions are enabled for the project.
- `caption_style` (object, optional, nullable) — Global styling to be applied to all captions
  - `template` (object, optional, nullable)
    - `key` (string, required)
    - `label` (string, required)
    - `requires_high_fps` (boolean, optional, default: false)
  - `text_font` (string, optional, nullable)
  - `text_scale` (double, optional, nullable)
  - `text_color` (string, optional, nullable)
  - `text_align` (enum, optional, nullable)
    - Allowed values: `start`, `center`, `end`
  - `text_style` (enum, optional, nullable)
    - Allowed values: `normal`, `italic`
  - `text_weight` (enum, optional, nullable)
    - Allowed values: `normal`, `bold`, `900`
  - `text_transform` (enum, optional, nullable)
    - Allowed values: `none`, `uppercase`
  - `text_blend_mode` (enum, optional, nullable)
    - Allowed values: `normal`, `difference`, `multiply`
  - `text_shadow` (object, optional, nullable)
    - `enabled` (boolean, required)
    - `color` (string, required)
    - `opacity` (double, required)
    - `blur` (double, required)
    - `offset_x` (double, required)
    - `offset_y` (double, required)
  - `text_outline` (object, optional, nullable)
    - `enabled` (boolean, required)
    - `color` (string, required)
    - `opacity` (double, required)
    - `width` (double, required)
  - `background_enabled` (boolean, optional, nullable)
  - `background_color` (string, optional, nullable)
  - `background_opacity` (double, optional, nullable)
  - `background_blur` (double, optional, nullable)
  - `background_border_radius` (double, optional, nullable)
  - `word_highlights_enabled` (boolean, optional, nullable)
  - `word_highlights_color` (string, optional, nullable)
  - `word_highlights_background_color` (string, optional, nullable)
  - `word_highlights_opacity` (double, optional, nullable)
  - `word_highlights_border_radius` (double, optional, nullable)
  - `word_highlights_blur` (double, optional, nullable)
  - `section_animation` (object, optional, nullable)
    - `enter_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `exit_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
  - `word_animation` (object, optional, nullable)
    - `enter_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `exit_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
  - `character_animation` (object, optional, nullable)
    - `enter_type` (enum, required)
      - Allowed values: `none`, `fade`, `typewriter`
    - `exit_type` (enum, required)
      - Allowed values: `none`, `fade`
  - `cursor_enabled` (boolean, optional, nullable)
  - `width_pct` (double, optional, nullable)
  - `horizontal_placement` (object, optional, nullable)
    - `align` (enum, required)
      - Allowed values: `left`, `center`, `right`
    - `translate_pct` (double, required)
  - `vertical_placement` (object, optional, nullable)
    - `align` (enum, required)
      - Allowed values: `top`, `center`, `bottom`
    - `translate_pct` (double, required)
  - `auto_break_enabled` (boolean, optional, nullable)
  - `max_lines_per_section` (integer, optional, nullable)
  - `max_words_per_line` (integer, optional, nullable)
- `caption_style_template_overrides` (map from string to object, optional, nullable) — Styling changes that have been made to the provided templates
  - `template` (object, optional, nullable)
    - `key` (string, required)
    - `label` (string, required)
    - `requires_high_fps` (boolean, optional, default: false)
  - `text_font` (string, optional, nullable)
  - `text_scale` (double, optional, nullable)
  - `text_color` (string, optional, nullable)
  - `text_align` (enum, optional, nullable)
    - Allowed values: `start`, `center`, `end`
  - `text_style` (enum, optional, nullable)
    - Allowed values: `normal`, `italic`
  - `text_weight` (enum, optional, nullable)
    - Allowed values: `normal`, `bold`, `900`
  - `text_transform` (enum, optional, nullable)
    - Allowed values: `none`, `uppercase`
  - `text_blend_mode` (enum, optional, nullable)
    - Allowed values: `normal`, `difference`, `multiply`
  - `text_shadow` (object, optional, nullable)
    - `enabled` (boolean, required)
    - `color` (string, required)
    - `opacity` (double, required)
    - `blur` (double, required)
    - `offset_x` (double, required)
    - `offset_y` (double, required)
  - `text_outline` (object, optional, nullable)
    - `enabled` (boolean, required)
    - `color` (string, required)
    - `opacity` (double, required)
    - `width` (double, required)
  - `background_enabled` (boolean, optional, nullable)
  - `background_color` (string, optional, nullable)
  - `background_opacity` (double, optional, nullable)
  - `background_blur` (double, optional, nullable)
  - `background_border_radius` (double, optional, nullable)
  - `word_highlights_enabled` (boolean, optional, nullable)
  - `word_highlights_color` (string, optional, nullable)
  - `word_highlights_background_color` (string, optional, nullable)
  - `word_highlights_opacity` (double, optional, nullable)
  - `word_highlights_border_radius` (double, optional, nullable)
  - `word_highlights_blur` (double, optional, nullable)
  - `section_animation` (object, optional, nullable)
    - `enter_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `exit_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
  - `word_animation` (object, optional, nullable)
    - `enter_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `exit_type` (enum, required)
      - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
  - `character_animation` (object, optional, nullable)
    - `enter_type` (enum, required)
      - Allowed values: `none`, `fade`, `typewriter`
    - `exit_type` (enum, required)
      - Allowed values: `none`, `fade`
  - `cursor_enabled` (boolean, optional, nullable)
  - `width_pct` (double, optional, nullable)
  - `horizontal_placement` (object, optional, nullable)
    - `align` (enum, required)
      - Allowed values: `left`, `center`, `right`
    - `translate_pct` (double, required)
  - `vertical_placement` (object, optional, nullable)
    - `align` (enum, required)
      - Allowed values: `top`, `center`, `bottom`
    - `translate_pct` (double, required)
  - `auto_break_enabled` (boolean, optional, nullable)
  - `max_lines_per_section` (integer, optional, nullable)
  - `max_words_per_line` (integer, optional, nullable)
- `public_share_id` (string, optional, nullable) — The public share ID of the project.
- `aspect_ratio` (enum, optional, nullable) — The aspect ratio of the project.
  - Allowed values: `16:9`, `9:16`, `4:5`, `1:1`
- `agent_settings` (object, optional, nullable) — Agent-related settings for the project
  - `tool_settings` (map from string to object, optional)
    - `skip_confirmation` (boolean, optional, default: false)
- `experimental` (map from string to any, optional) — Experimental features for the project.
- `base_voices` (list of object, optional, nullable) — List of voices used by the project.
  - `voice_id` (string, required) — The ID of the voice.
  - `name` (string, optional) — The name of the voice.
  - `samples` (list of object, optional, nullable) — List of samples associated with the voice.
    - `sample_id` (string, optional) — The ID of the sample.
    - `file_name` (string, optional) — The name of the sample file.
    - `mime_type` (string, optional) — The MIME type of the sample file.
    - `size_bytes` (integer, optional) — The size of the sample file in bytes.
    - `hash` (string, optional) — The hash of the sample file.
    - `duration_secs` (double, optional, nullable)
    - `remove_background_noise` (boolean, optional, nullable)
    - `has_isolated_audio` (boolean, optional, nullable)
    - `has_isolated_audio_preview` (boolean, optional, nullable)
    - `speaker_separation` (object, optional, nullable)
      - `voice_id` (string, required) — The ID of the voice.
      - `sample_id` (string, required) — The ID of the sample.
      - `status` (enum, required) — The status of the speaker separation.
        - Allowed values: `not_started`, `pending`, `completed`, `failed`
      - `speakers` (map from string to object, optional, nullable) — The speakers of the sample.
        - `speaker_id` (string, required) — The ID of the speaker.
        - `duration_secs` (double, required) — The duration of the speaker segment in seconds.
        - `utterances` (list of object, optional, nullable) — The utterances of the speaker.
          - `start` (double, required) — The start time of the utterance in seconds.
          - `end` (double, required) — The end time of the utterance in seconds.
      - `selected_speaker_ids` (list of string, optional, nullable) — The IDs of the selected speakers.
    - `trim_start` (integer, optional, nullable)
    - `trim_end` (integer, optional, nullable)
  - `category` (enum, optional) — The category of the voice.
    - Allowed values: `generated`, `cloned`, `premade`, `professional`, `famous`, `high_quality`
  - `fine_tuning` (object, optional, nullable) — Fine-tuning information for the voice.
    - `is_allowed_to_fine_tune` (boolean, optional) — Whether the user is allowed to fine-tune the voice.
    - `state` (map from string to enum, optional) — The state of the fine-tuning process for each model.
      - Allowed values: `not_started`, `queued`, `fine_tuning`, `fine_tuned`, `failed`, `delayed`
    - `verification_failures` (list of string, optional) — List of verification failures in the fine-tuning process.
    - `verification_attempts_count` (integer, optional) — The number of verification attempts in the fine-tuning process.
    - `manual_verification_requested` (boolean, optional) — Whether a manual verification was requested for the fine-tuning process.
    - `language` (string, optional, nullable) — The language of the fine-tuning process.
    - `progress` (map from string to double, optional, nullable) — The progress of the fine-tuning process.
    - `message` (map from string to string, optional, nullable) — The message of the fine-tuning process.
    - `dataset_duration_seconds` (double, optional, nullable) — The duration of the dataset in seconds.
    - `verification_attempts` (list of object, optional, nullable) — The number of verification attempts.
      - `text` (string, required) — The text of the verification attempt.
      - `date_unix` (integer, required) — The date of the verification attempt in Unix time.
      - `accepted` (boolean, required) — Whether the verification attempt was accepted.
      - `similarity` (double, required) — The similarity of the verification attempt.
      - `levenshtein_distance` (double, required) — The Levenshtein distance of the verification attempt.
      - `recording` (object, optional, nullable) — The recording of the verification attempt.
        - `recording_id` (string, required) — The ID of the recording.
        - `mime_type` (string, required) — The MIME type of the recording.
        - `size_bytes` (integer, required) — The size of the recording in bytes.
        - `upload_date_unix` (integer, required) — The date of the recording in Unix time.
        - `transcription` (string, required) — The transcription of the recording.
    - `slice_ids` (list of string, optional, nullable) — List of slice IDs.
    - `manual_verification` (object, optional, nullable) — The manual verification of the fine-tuning process.
      - `extra_text` (string, required) — The extra text of the manual verification.
      - `request_time_unix` (integer, required) — The date of the manual verification in Unix time.
      - `files` (list of object, required) — The files of the manual verification.
        - `file_id` (string, required) — The ID of the file.
        - `file_name` (string, required) — The name of the file.
        - `mime_type` (string, required) — The MIME type of the file.
        - `size_bytes` (integer, required) — The size of the file in bytes.
        - `upload_date_unix` (integer, required) — The date of the file in Unix time.
    - `max_verification_attempts` (integer, optional, nullable) — The maximum number of verification attempts.
    - `next_max_verification_attempts_reset_unix_ms` (integer, optional, nullable) — The next maximum verification attempts reset time in Unix milliseconds.
    - `finetuning_state` (any, optional)
  - `labels` (map from string to string, optional) — Labels associated with the voice.
  - `description` (string, optional, nullable) — The description of the voice.
  - `preview_url` (string, optional, nullable) — The preview URL of the voice.
  - `available_for_tiers` (list of string, optional) — The tiers the voice is available for.
  - `settings` (object, optional, nullable) — The settings of the voice.
    - `stability` (double, optional, nullable, default: 0.5) — Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.
    - `use_speaker_boost` (boolean, optional, nullable, default: true) — This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency.
    - `similarity_boost` (double, optional, nullable, default: 0.75) — Determines how closely the AI should adhere to the original voice when attempting to replicate it.
    - `style` (double, optional, nullable, default: 0) — Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0.
    - `speed` (double, optional, nullable, default: 1) — Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up.
  - `sharing` (object, optional, nullable) — The sharing information of the voice.
    - `status` (enum, optional) — The status of the voice sharing.
      - Allowed values: `enabled`, `disabled`, `copied`, `copied_disabled`
    - `history_item_sample_id` (string, optional, nullable) — The sample ID of the history item.
    - `date_unix` (integer, optional) — The date of the voice sharing in Unix time.
    - `whitelisted_emails` (list of string, optional) — A list of whitelisted emails.
    - `public_owner_id` (string, optional) — The ID of the public owner.
    - `original_voice_id` (string, optional) — The ID of the original voice.
    - `financial_rewards_enabled` (boolean, optional) — Whether financial rewards are enabled.
    - `free_users_allowed` (boolean, optional) — Whether free users are allowed.
    - `live_moderation_enabled` (boolean, optional) — Whether live moderation is enabled.
    - `rate` (double, optional, nullable) — The rate of the voice sharing.
    - `fiat_rate` (double, optional, nullable) — The rate of the voice sharing in USD per 1000 credits.
    - `notice_period` (integer, optional) — The notice period of the voice sharing.
    - `disable_at_unix` (integer, optional, nullable) — The date of the voice sharing in Unix time.
    - `voice_mixing_allowed` (boolean, optional) — Whether voice mixing is allowed.
    - `featured` (boolean, optional) — Whether the voice is featured.
    - `category` (enum, optional) — The category of the voice.
      - Allowed values: `generated`, `cloned`, `premade`, `professional`, `famous`, `high_quality`
    - `reader_app_enabled` (boolean, optional, nullable) — Whether the reader app is enabled.
    - `image_url` (string, optional, nullable) — The image URL of the voice.
    - `ban_reason` (string, optional, nullable) — The ban reason of the voice.
    - `liked_by_count` (integer, optional) — The number of likes on the voice.
    - `cloned_by_count` (integer, optional) — The number of clones on the voice.
    - `name` (string, optional) — The name of the voice.
    - `description` (string, optional, nullable) — The description of the voice.
    - `labels` (map from string to string, optional) — The labels of the voice.
    - `review_status` (enum, optional) — The review status of the voice.
      - Allowed values: `not_requested`, `pending`, `declined`, `allowed`, `allowed_with_changes`
    - `review_message` (string, optional, nullable) — The review message of the voice.
    - `enabled_in_library` (boolean, optional) — Whether the voice is enabled in the library.
    - `instagram_username` (string, optional, nullable) — The Instagram username of the voice.
    - `twitter_username` (string, optional, nullable) — The Twitter/X username of the voice.
    - `youtube_username` (string, optional, nullable) — The YouTube username of the voice.
    - `tiktok_username` (string, optional, nullable) — The TikTok username of the voice.
    - `moderation_check` (object, optional, nullable) — The moderation check of the voice.
      - `date_checked_unix` (integer, optional, nullable) — The date the moderation check was made in Unix time.
      - `name_value` (string, optional, nullable) — The name value of the voice.
      - `name_check` (boolean, optional, nullable) — Whether the name check was successful.
      - `description_value` (string, optional, nullable) — The description value of the voice.
      - `description_check` (boolean, optional, nullable) — Whether the description check was successful.
      - `sample_ids` (list of string, optional, nullable) — A list of sample IDs.
      - `sample_checks` (list of double, optional, nullable) — A list of sample checks.
      - `captcha_ids` (list of string, optional, nullable) — A list of captcha IDs.
      - `captcha_checks` (list of double, optional, nullable) — A list of CAPTCHA check values.
    - `reader_restricted_on` (list of object, optional, nullable) — The reader restricted on of the voice.
      - `resource_type` (enum, required) — The type of resource.
        - Allowed values: `read`, `collection`
      - `resource_id` (string, required) — The ID of the resource.
  - `high_quality_base_model_ids` (list of string, optional) — The base model IDs for high-quality voices.
  - `verified_languages` (list of object, optional, nullable) — The verified languages of the voice.
    - `language` (string, required) — The language of the voice.
    - `model_id` (string, required) — The voice's model ID.
    - `accent` (string, optional, nullable) — The voice's accent, if applicable.
    - `locale` (string, optional, nullable) — The voice's locale, if applicable.
    - `preview_url` (string, optional, nullable) — The voice's preview URL, if applicable.
  - `collection_ids` (list of string, optional, nullable) — The IDs of collections this voice belongs to.
  - `safety_control` (enum, optional, nullable) — The safety controls of the voice.
    - Allowed values: `NONE`, `BAN`, `CAPTCHA`, `ENTERPRISE_BAN`, `ENTERPRISE_CAPTCHA`
  - `voice_verification` (object, optional, nullable) — The voice verification of the voice.
    - `requires_verification` (boolean, required) — Whether the voice requires verification.
    - `is_verified` (boolean, required) — Whether the voice has been verified.
    - `verification_failures` (list of string, required) — List of verification failures.
    - `verification_attempts_count` (integer, required) — The number of verification attempts.
    - `language` (string, optional, nullable) — The language of the voice.
    - `verification_attempts` (list of object, optional, nullable) — Number of times a verification was attempted.
      - `text` (string, required) — The text of the verification attempt.
      - `date_unix` (integer, required) — The date of the verification attempt in Unix time.
      - `accepted` (boolean, required) — Whether the verification attempt was accepted.
      - `similarity` (double, required) — The similarity of the verification attempt.
      - `levenshtein_distance` (double, required) — The Levenshtein distance of the verification attempt.
      - `recording` (object, optional, nullable) — The recording of the verification attempt.
        - `recording_id` (string, required) — The ID of the recording.
        - `mime_type` (string, required) — The MIME type of the recording.
        - `size_bytes` (integer, required) — The size of the recording in bytes.
        - `upload_date_unix` (integer, required) — The date of the recording in Unix time.
        - `transcription` (string, required) — The transcription of the recording.
  - `permission_on_resource` (string, optional, nullable) — The permission on the resource of the voice.
  - `is_owner` (boolean, optional, nullable) — Whether the voice is owned by the user.
  - `is_legacy` (boolean, optional, default: false) — Whether the voice is legacy.
  - `is_mixed` (boolean, optional, default: false) — Whether the voice is mixed.
  - `favorited_at_unix` (integer, optional, nullable) — Timestamp when the voice was marked as favorite in Unix time.
  - `created_at_unix` (integer, optional, nullable) — The creation time of the voice in Unix time.
  - `is_bookmarked` (boolean, optional, nullable) — Whether the voice is bookmarked by the current user. Only relevant for community (library-copied) voices.
  - `recording_quality` (enum, optional, nullable) — The recording quality of the voice as determined by the review pipeline.
    - Allowed values: `studio`, `good`, `ok`, `poor`, `bad`
  - `labelling_status` (enum, optional, nullable) — The review pipeline status of the voice.
    - Allowed values: `in_review`, `review_complete`
  - `recording_quality_reason` (string, optional, nullable) — The reason for the recording quality assessment, as determined by the review pipeline.
- `publishing_read` (object, optional, nullable) — The ElevenReader data if the book was published.
  - `read_id` (string, required)
  - `created_at_unix` (integer, required)
  - `updated_at_unix` (integer, required)
  - `word_count` (integer, required)
  - `char_count` (integer, required)
  - `chapters` (list of object, required)
    - `chapter_name` (string, required)
    - `word_count` (integer, required)
    - `char_count` (integer, required)
    - `starting_char_offset` (integer, required)
    - `has_parsed_html` (boolean, optional, default: false)
    - `has_summary` (boolean, optional, default: false)
    - `duration_seconds` (double, optional, nullable)
    - `file_number` (string, optional, nullable)
    - `is_fallback_name` (boolean, optional, default: false)
    - `chapter_id` (string, optional, nullable)
  - `title` (string, optional, nullable)
  - `author` (string, optional, nullable)
  - `description` (string, optional, nullable)
  - `article_image_url` (string, optional, nullable)
  - `language` (string, optional, nullable)
  - `locale` (string, optional, nullable)
  - `display_mode` (enum, optional, nullable)
    - Allowed values: `text`, `audio-only`, `text-with-audio`
  - `genre` (list of enum, optional, nullable)
    - Allowed values: `Fantasy`, `Romance`, `Science Fiction`, `Mystery and Thriller`, `Action and Adventure`, `Dystopia`, `Business and Economics`, `Technology`, `Christian & Inspirational`, `Horror`, `Biography and Memoir`, `Education and Learning`, `History`, `Children's Literature`, `Young Adult`, `Fairy Tales and Folklore`, `Fan Fiction`, `General Fiction`, `Health and Wellness`, `Historical Fiction`, `Humor`, `Literary Classics`, `Philosophy`, `Poetry`, `Politics and Government`, `Psychology`, `Science and Nature`, `Self-Help`, `Spirituality and Religion`, `Travel`, `True Crime`, `Other`
  - `fiction` (string, optional, nullable)
  - `content_type` (string, optional, nullable)
  - `original_file_type` (string, optional, nullable)
  - `target_audience` (enum, optional, nullable)
    - Allowed values: `children`, `young adult`, `adult`, `all ages`
  - `mature_content` (boolean, optional, nullable)
  - `safesearch_adult` (boolean, optional, nullable)
  - `origin` (string, optional, nullable)
  - `publication_date` (string, optional, nullable)
  - `isbn` (string, optional, nullable)
  - `ean` (string, optional, nullable)
  - `legal_terms` (object, optional, nullable)
    - `terms` (string, optional, nullable)
    - `start_date` (string, optional, nullable)
    - `end_date` (string, optional, nullable)
  - `content_guidelines_terms` (object, optional, nullable)
    - `terms` (string, optional, nullable)
    - `start_date` (string, optional, nullable)
    - `end_date` (string, optional, nullable)
  - `last_updated_from_project_unix` (integer, optional, nullable)
  - `publishing_project_id` (string, optional, nullable)
  - `publishing_state` (string, optional, default: published)
  - `publisher_profile_id` (string, optional, nullable)
  - `quality_score` (integer, optional, nullable)
  - `publisher` (string, optional, nullable)
  - `copyright` (string, optional, nullable)
  - `subtitle` (string, optional, nullable)
  - `distribution_territories` (list of string, optional, nullable)
  - `edition` (string, optional, nullable)
  - `contributors` (list of object, optional, nullable)
    - `name` (string, required)
    - `role` (string, required)
    - `bio` (string, optional, nullable)
    - `profile_id` (string, optional, nullable)
  - `payout_type` (enum, optional, nullable)
    - Allowed values: `none`, `engagement_based`, `fixed_payout`
  - `list_price` (double, optional, nullable)
  - `currency` ("usd", optional, nullable)
  - `original_audio_project_export_id` (string, optional, nullable)
  - `original_audio_document_id` (string, optional, nullable)
  - `series_id` (string, optional, nullable)
  - `volume` (integer, optional, nullable)
  - `published_at_unix` (integer, optional, nullable)
  - `read_slug` (string, optional, nullable)
  - `preview_audio_object` (object, optional, nullable)
    - `audio_url` (string, required)
    - `voice_id` (string, optional, nullable)
    - `text` (string, optional, nullable)
    - `hls_manifest_url` (string, optional, nullable)
    - `dash_manifest_url` (string, optional, nullable)
    - `is_auto_generated` (boolean, optional, nullable, default: false)
    - `generated_at_unix` (integer, optional, nullable)
  - `sample_config` (object, optional, nullable)
    - `is_sample` (boolean, optional, default: false)
    - `parent_id` (string, optional, nullable)
    - `parent_type` (enum, optional, nullable)
      - Allowed values: `read`, `collection`
    - `chapter_ids` (list of string, optional, nullable)
  - `review` (object, optional, nullable)
    - `review_status` (enum, required)
      - Allowed values: `approved`, `edits_required`, `rejected`
    - `reviewed_at_unix` (integer, required)
    - `reviewed_by` (string, optional, nullable)
    - `reject_reasons` (list of enum, optional, nullable)
      - Allowed values: `lacks_structure`, `doesnt_open`, `not_literary_work`, `language_not_supported`, `too_short`, `duplicate`, `promotional`, `formatting_issues`, `low_quality`, `metadata_incomplete`, `metadata_inaccurate`, `typos`, `review_error`, `spam`, `legal_violation`, `content_policy`, `public_domain`, `other`
    - `scores_breakdown` (map from string to integer, optional, nullable)
    - `rejected_details` (string, optional, nullable)
    - `explanation` (string, optional, nullable)
  - `voice_id` (string, optional, nullable)
  - `can_use_assistant` (boolean, optional, default: true)
  - `is_voice_changer_on` (boolean, optional, default: false)
  - `restricted_to_user_email_domains` (list of string, optional, nullable)

## Examples

**Response**

```json
{
  "project_id": "aw1NgEzBg83R7vgmiJt6",
  "name": "My Project",
  "create_date_unix": 1714204800,
  "created_by_user_id": "Vbtgl3bRdj6lk79rYAgx",
  "default_title_voice_ref_id": "JBFqnCBsd6RMkjVDRZzb",
  "default_paragraph_voice_ref_id": "JBFqnCBsd6RMkjVDRZzb",
  "default_model_id": "eleven_multilingual_v2",
  "can_be_downloaded": true,
  "volume_normalization": true,
  "state": "default",
  "access_level": "viewer",
  "quality_preset": "standard",
  "chapters": [
    {
      "chapter_id": "aw1NgEzBg83R7vgmiJt6",
      "name": "Chapter 1",
      "can_be_downloaded": true,
      "state": "converting",
      "last_conversion_date_unix": 1714204800,
      "conversion_progress": 0.5,
      "statistics": {
        "characters_unconverted": 1000,
        "characters_converted": 500,
        "paragraphs_converted": 20,
        "paragraphs_unconverted": 10,
        "credits_needed_to_convert": 1000,
        "voice_statistics": [
          {
            "project_voice_ref_id": "voice123",
            "characters_unconverted": 600,
            "characters_converted": 300,
            "voice_id": "voice123"
          },
          {
            "project_voice_ref_id": "voice456",
            "characters_unconverted": 400,
            "characters_converted": 200,
            "voice_id": "voice456"
          }
        ]
      },
      "last_conversion_error": "Error message"
    }
  ],
  "pronunciation_dictionary_versions": [],
  "pronunciation_dictionary_locators": [],
  "apply_text_normalization": "auto",
  "assets": [],
  "voices": [],
  "quality_check_on": false,
  "quality_check_on_when_bulk_convert": false,
  "default_title_voice_id": "JBFqnCBsd6RMkjVDRZzb",
  "default_paragraph_voice_id": "JBFqnCBsd6RMkjVDRZzb",
  "last_conversion_date_unix": 1714204800,
  "title": "My Project",
  "author": "John Doe",
  "description": "This is a description of my project.",
  "genres": [
    "Novel",
    "Short Story"
  ],
  "cover_image_url": "https://example.com/cover.jpg",
  "target_audience": "young adult",
  "language": "en",
  "content_type": "Novel",
  "original_publication_date": "2025-01-01",
  "mature_content": false,
  "isbn_number": "978-90-274-3964-2",
  "fiction": "fiction",
  "creation_meta": {
    "creation_progress": 0.5,
    "status": "pending",
    "type": "blank"
  },
  "public_share_id": "abc123def456789",
  "experimental": {},
  "base_voices": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.get("project_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.get(
    project_id="project_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
